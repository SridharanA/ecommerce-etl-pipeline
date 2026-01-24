FROM python:3.9-slim

WORKDIR /home/app

COPY . .

RUN pip install streamlit pandas requests

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]