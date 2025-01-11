FROM python:3.9
WORKDIR C:/скил/DST-156/IDE_NEW/DS_PROD-2. Воспроизводимость и контейнеризация приложений/web/src/app
COPY ./app ./
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./server.py" ]