SignBank
========

SignBank is a web based sign language dictionary.  It was developed to support
the Auslan SignBank but is now being used with BSL.  

To build:

```[shell]
$ docker build -f Dockerfile -t docker.pkg.github.com/stevecassidy/signbank-modular/signbank:latest . 
$ docker login docker.pkg.github.com -u stevecassidy -p <token>
$ docker push docker.pkg.github.com/stevecassidy/signbank-modular/signbank:latest
```

On the host:

```[shell]
$ docker login docker.pkg.github.com -u stevecassidy -p <token>
$ docker pull docker.pkg.github.com/stevecassidy/signbank-modular/signbank:latest
$ docker run -d --env-file env.prod -p 8000:9000  docker.pkg.github.com/stevecassidy/signbank-modular/signbank:latest gunicorn --bind=0.0.0.0  signbank.wsgi
```

Create database user with a password (under the postgres account):

```[shell]
$ createuser -P -s -e auslan
```

Create database (again as postgres):

```[shell]
createdb auslan
```

Restore database from backup (as root)

```[shell]
$ zcat auslan_production-20201206.sql.gz  | psql -U auslan -W --host=localhost
```
