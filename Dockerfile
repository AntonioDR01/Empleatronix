FROM python:3.12
WORKDIR /app
COPY requiremets.txt .
RUN pip install -r requiremets.txt
ENTRYPOINT ["streamlit", "run", "app.py"]