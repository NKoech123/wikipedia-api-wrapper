FROM python:3.10-alpine
WORKDIR /app
RUN pip3 install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN python3 -m pip install -r /app/requirements.txt
COPY .  /app 
CMD ["main.py"]