FROM python:3.11.4

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash", "./shell_scripts/run.sh"]


