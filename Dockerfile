FROM python
RUN pip install streamlit matplotlib
WORKDIR /app
ENTRYPOINT ["streamlit", "run", "app.py"]