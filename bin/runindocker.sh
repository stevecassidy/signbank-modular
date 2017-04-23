python bin/docker.py migrate
python bin/docker.py collectstatic --noinput
python bin/docker.py runserver 0.0.0.0:8000
