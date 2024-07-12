FROM python:3.10-slim
RUN mkdir /site
COPY . /site/


WORKDIR /site
RUN pip install django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

