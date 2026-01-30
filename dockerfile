FROM python:3.13
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000


ENV FLASK_RUN_HOST=0.0.0.0
ENV PORT=5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]