FROM mariadb:latest

ARG ${root}
ARG ${1234}

# MariaDB 구성
ENV MYSQL_ROOT_PASSWORD=1234

ADD create_database.sql /docker-entrypoint-initdb.d/create_database.sql

EXPOSE 3306