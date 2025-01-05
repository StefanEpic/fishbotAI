FROM ubuntu:22.04

WORKDIR /root

RUN apt-get update && apt-get upgrade && apt-get install -y python3.10 python3-pip libgl1-mesa-glx libglib2.0-0

COPY requirements.txt .
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install -r requirements.txt
RUN mkdir temp

COPY utils.py .
COPY api.py .
COPY neuro.py .
COPY model.pt .

CMD gunicorn api:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --forwarded-allow-ips='*' --bind=0.0.0.0:8000
