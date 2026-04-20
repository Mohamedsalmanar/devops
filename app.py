from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
REQUESTS = Counter('requests_total', 'Total requests')

@app.route("/")
def home():
    REQUESTS.inc()
    return "Hello DevOps!"

@app.route("/metrics")
def metrics():
    return generate_latest()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
