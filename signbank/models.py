"""
A model (``RegistrationProfile``) for storing user-registration data,
and an associated custom manager (``RegistrationManager``).

"""

import time
import re
import string
from django.conf import settings
from django.db import models
from django.contrib.auth import models as authmodels
from django import forms
from django.utils.translation import ugettext_lazy as _


def t(message):
    """Replace $country and $language in message with dat from settings"""

    tpl = string.Template(message)
    return tpl.substitute(country=settings.COUNTRY_NAME, language=settings.LANGUAGE_NAME)


backgroundChoices = ((0, 'deaf community'),
                     (1, t('$language teacher')),
                     (2, 'teacher of the deaf'),
                     (3, 'parent of a deaf child'),
                     (4, 'sign language interpreter'),
                     (5, 'school or college student (under 18)'),
                     (6, t('student learning $language')),
                     (9, 'university student (taught, e.g. BA, BSc, MA, Msc)'),
                     (10, 'university student (research, e.g. PhD)'),
                     (8, 'university academic/research staff'),
                     (7, 'other'),
                     )

learnedChoices = ((0, 'Not Applicable'),
                  (1, 'At home from my parent(s)'),
                  (2, 'At kindergarten or at the beginning of primary school'),
                  (3, 'At primary school'),
                  (4, 'At high school'),
                  (5, 'After I left school'),
                  )

schoolChoices = ((0, 'a deaf school (boarder)'),
                 (1, 'a deaf school (day student)'),
                 (2, 'a deaf classroom or unit in a hearing school'),
                 (3, 'a regular classroom in a hearing school'),
                 )

teachercommChoices = ((0, 'mostly oral'),
                      (1, 'mostly Signed English'),
                      (2, t('mostly sign language ($language)')),
                      (3, 'mostly fingerspelling'),
                      (4, 'N/A, I am hearing')
                      )

yesnoChoices = ((1, 'yes'), (0, 'no'))


class UserProfile(models.Model):
    """Extended profile for users of the site"""

    user = models.OneToOneField(authmodels.User, on_delete=models.CASCADE)

    yob = models.IntegerField("When were you born?")
    australian = models.BooleanField(t("Do you live in $country?"))
    postcode = models.CharField(t("If you live in $country, what is your postcode?"), max_length=20, blank=True)
    background = models.CharField("What is your background?", max_length=20, choices=backgroundChoices)
    researcher_credentials = models.TextField(t("Research credentials"))
    auslan_user = models.BooleanField(t("Do you use $language?"))
    learned = models.IntegerField(t("If you use $language, when did you learn sign language?"),
                                  choices=learnedChoices)
    deaf = models.BooleanField("Are you a deaf person?")
    schooltype = models.IntegerField("What sort of school do you (or did you) attend?",
                                     choices=schoolChoices)
    school = models.CharField("Which school do you (or did you) attend?", max_length=50, blank=True)
    teachercomm = models.IntegerField("How do (or did) your teachers communicate with you?",
                                      choices=teachercommChoices)

    @staticmethod
    def best_describes_you_from_background(background):
        result = []
        try:
            indices = background.split(",")
            for index in indices:
                i = int(''.join(n for n in index if n.isdigit()))
                result.append(dict(backgroundChoices)[i])
        except:
            result = ['(unknown)']
        return ", ".join(result)

    def best_describes_you(self):
        "Return the background in a readable form"
        return UserProfile.best_describes_you_from_background(self.background)

    @staticmethod
    def is_researcher_from_background(background):
        return 'research' in UserProfile.best_describes_you_from_background(background)

    def is_researcher(self):
        "True if this person has picked a background that includes the word research"
        return UserProfile.is_researcher_from_background(self.background)

    class Admin:
        list_display = ['user', 'deaf', 'auslan_user']


class BirthYearField(forms.Field):
    """A form field for entry of a year of birth,
     must be before this year and not more than 110 years ago"""

    year_re = re.compile("\d\d\d\d")

    def clean(self, value):
        if not value:
            raise forms.ValidationError('Enter a four digit year, eg. 1984.')

        if not self.year_re.match(str(value)):
            raise forms.ValidationError('%s is not a valid year.' % value   )
        year = int(value)
        # check not after this year
        thisyear = time.localtime()[0]
        if year > thisyear:
            raise forms.ValidationError("%s is in the future, please enter your year of birth." % value )
        # or that this person isn't over 110
        if year < thisyear-110:
            raise forms.ValidationError("If you were born in %s you are now %s years old! Please enter your real birth year." % (year, thisyear-year))
        return year


class RegistrationForm(forms.Form):
    """
    Registration form for the site
    """
    username = forms.CharField(widget=forms.HiddenInput, required=False)
    first_name = forms.CharField(label=t("Firstname"), max_length=50)

    last_name = forms.CharField(label=t("Lastname"), max_length=50)

    yob = BirthYearField(label=t("What year were you born?"))

    australian = forms.ChoiceField(yesnoChoices, label=t("Do you live in ${country}?"))

    postcode = forms.CharField(label=t("If you live in $country, what is your postcode?"),
                               max_length=20, required=False)

    background = forms.MultipleChoiceField(backgroundChoices, label=_("Which of the following best describes you?"))

    researcher_credentials = forms.CharField(label=t("(OPTIONAL) If you would like access to advanced SignBank features, e.g. advanced search and detail view of signs, please give evidence of your researcher status here (e.g. link to your university staff profile page, or evidence that you are a research student)."), widget=forms.Textarea, required=False)

    auslan_user = forms.ChoiceField(yesnoChoices, label=t("Do you use $language?"), required=False)

    learned = forms.ChoiceField(label=t("If you use $language, when did you learn sign language?"),
                                choices=learnedChoices, required=False)

    deaf = forms.ChoiceField(yesnoChoices, label=t("Are you a deaf person?"))

    schooltype = forms.ChoiceField(label=t("What sort of school do you (or did you) attend?"),
                                   choices=schoolChoices, required=False)
    school = forms.CharField(label=t("Which school do you (or did you) attend?"),
                             max_length=50, required=False)
    teachercomm = forms.ChoiceField(label=t("How do (or did) your teachers communicate with you?"),
                                    choices=teachercommChoices,
                                    required=False)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        # Get the indices of the selected backgrounds to help decide if this is a researcher
        background_list = ",".join(self.cleaned_data['background'])

        profile = UserProfile(user=user,
                              yob=self.cleaned_data['yob'],
                              australian=self.cleaned_data['australian'] == '1',
                              postcode=self.cleaned_data['postcode'],
                              background=background_list,
                              researcher_credentials=self.cleaned_data['researcher_credentials'],
                              auslan_user=self.cleaned_data['auslan_user'] == '1',
                              learned=self.cleaned_data['learned'],
                              deaf=self.cleaned_data['deaf'] == '1',
                              schooltype=self.cleaned_data['schooltype'],
                              school=self.cleaned_data['school'],
                              teachercomm=self.cleaned_data['teachercomm'])

        profile.save()



        user.save()
