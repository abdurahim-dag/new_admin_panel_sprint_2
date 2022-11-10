FROM python:3.10

ARG appuser
RUN useradd -U $appuser

WORKDIR /app
COPY . .

#ENV DJANGO_SETTINGS_MODULE 'config.settings'

RUN  mkdir -p /app/media \
     && chown $appuser:$appuser /app/media \
     && mkdir -p /app/static \
     && chown $appuser:$appuser /app/static \
     && pip install --upgrade pip \
     && pip install -r requirements.txt \
     && chown $appuser:$appuser -R /app

EXPOSE 8000

USER $appuser

ENTRYPOINT ["/app/run.sh"]