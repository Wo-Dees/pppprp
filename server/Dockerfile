FROM python:3.8-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY server.py server.py

CMD ["python", "server.py"]


