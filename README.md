# DevOps Project: Flask App with CI/CD, Monitoring & Cloudflare Tunnel
https://devsalman.space/

## Overview

This project demonstrates a complete DevOps pipeline:

* Flask application (Python)
* Dockerized deployment
* CI/CD using GitHub Actions
* Monitoring using Prometheus & Grafana
* Secure public access using Cloudflare Tunnel (no public IP)

---

## Architecture

```
User → Cloudflare → Tunnel → Docker Containers
                             ├── Flask App (5000)
                             ├── Grafana (3000)
                             └── Prometheus (9090)
```

---

## Tech Stack

* Python (Flask)
* Docker
* GitHub Actions (CI/CD)
* Prometheus
* Grafana
* Cloudflare Tunnel

---

## CI/CD Pipeline

On every push to `main`:

1. Build Docker image
2. Push image to Docker Hub
3. Deploy automatically via self-hosted runner

---

## Docker Setup

Build and run:

```
docker build -t myapp .
docker run -d -p 5000:5000 myapp
```

---

## Monitoring

* Prometheus scrapes `/metrics`
* Grafana visualizes:

  * request count
  * uptime
  * system metrics

---

## Public Access (No Public IP)

Using Cloudflare Tunnel:

```
https://yourdomain.com            → Flask app
https://grafana.yourdomain.com    → Grafana
https://prometheus.yourdomain.com → Prometheus
```

---

## Security

* No open ports on server
* Access via secure tunnel
* Optional: Cloudflare Access for authentication

---

## Example Metrics

* `requests_total`
* `process_cpu_seconds_total`
* `process_resident_memory_bytes`

---

 Grafana dashboard
 <img width="1545" height="437" alt="image" src="https://github.com/user-attachments/assets/b6b92e3d-0237-4713-806c-424bef94fcdc" />

