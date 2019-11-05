FROM python:3.7-alpine
COPY . ./app/
COPY docker/entrypoint.sh ./app/
WORKDIR app/
RUN pip install -r requirements.txt
ENTRYPOINT ["sh", "entrypoint.sh"]
