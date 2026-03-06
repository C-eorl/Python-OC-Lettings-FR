FROM python:3.10-slim
LABEL authors="ceorl"
LABEL description="OC Lettings Site"

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn

COPY .. .

RUN python manage.py collectstatic --noinput

ENV PORT 8000

CMD ["sh", "-c", "gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT --workers 3 --timeout 120"]