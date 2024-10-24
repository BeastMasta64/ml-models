FROM postgres:14.5-alpine

ENV POSTGRES_HOST db_results
ENV POSTGRES_PORT 5432
ENV POSTGRES_DB result
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres

COPY init.sql /docker-entrypoint-initdb.d/init.sql