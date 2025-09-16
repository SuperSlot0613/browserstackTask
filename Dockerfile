FROM python:3.11-slim

WORKDIR /BowserStackTask

RUN apt-get update && apt-get install -y \
    wget curl unzip git ca-certificates libcairo2 \
    libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libxkbcommon0 \
    libxcomposite1 libxrandr2 libxdamage1 libxfixes3 libxext6 \
    libgbm1 libpango-1.0-0 libasound2 libx11-xcb1 libxcb1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# ✅ Copy pre-downloaded browsers
#COPY --from=browsers /root/.cache/ms-playwright /root/.cache/ms-playwright

COPY . .
ENV PYTHONPATH=/BowserStackTask

CMD ["pytest", "-s","-v"]
#CMD ["bash", "-c", "playwright install chromium --with-deps && python CC_Script/MainPy.py"]