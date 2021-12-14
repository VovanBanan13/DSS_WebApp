FROM python:3.8

COPY . /app
WORKDIR /app

# virtualenv venv
RUN python3 -m venv venv
CMD  ["source venv/bin/activate"]

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod +x start.sh

ENTRYPOINT ["/bin/bash", "start.sh"]

EXPOSE 5000