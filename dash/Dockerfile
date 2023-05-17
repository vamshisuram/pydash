FROM python:3.9

WORKDIR /dash

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "dash.py", "--server.port=8000", "--server.address=0.0.0.0"]
