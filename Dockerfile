FROM python:3.11.4

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 18000

ENTRYPOINT [ "bash", "./shell_scripts/run.sh"]



