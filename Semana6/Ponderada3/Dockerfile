FROM python:3.8-slim-buster

WORKDIR /app

RUN pip3 freeze > requirements.txt && pip install uvicorn && pip install fastapi

COPY . .

CMD [ "uvicorn", "api:app","--reload"]

EXPOSE 8000