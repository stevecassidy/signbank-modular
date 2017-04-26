from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

# http://stackoverflow.com/questions/37332190/django-login-with-email

class EmailBackend(ModelBackend):

  def authenticate(self, username=None, password=None, **kwargs):

    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(email__iexact=username)
    except UserModel.DoesNotExist:
        return None
    else:
        if getattr(user, 'is_active', False) and  user.check_password(password):
            return user
    return None
