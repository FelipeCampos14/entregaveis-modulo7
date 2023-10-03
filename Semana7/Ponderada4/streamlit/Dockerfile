FROM python:latest

WORKDIR /code

COPY . . 

RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run","streamlit.py"]