FROM python:latest

WORKDIR /app
COPY app.py /app
COPY requirements.txt /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
CMD python app.py
