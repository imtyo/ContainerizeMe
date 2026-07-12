# ContainerizeMe

Automatically generate Docker and deployment configuration files for existing Python APIs.

ContainerizeMe scans a Flask or FastAPI project and generates:

- Dockerfile
- docker-compose.yml

without manually writing boilerplate configuration.

---

## Features

### Current Features

- Detect Flask applications
- Detect FastAPI applications
- Detect application entrypoint
- Detect application port
- Generate Dockerfile
- Generate docker-compose.yml

### Planned Features

- Generate .gitlab-ci.yml
- Recursive project scanning
- Environment variable detection
- Kubernetes deployment templates
- GitHub Actions workflow generation

---

## Supported Frameworks

| Framework | Supported |
|------------|------------|
| Flask | ✅ |
| FastAPI | ✅ |
| Django | ⏳ |
| Falcon | ⏳ |

---

## Project Structure

```text
containerizeme/
│
├── test/
│   ├── flask-api/
│   └── fastapi-api/
│
├── generators/
│   ├── detector.py
│   ├── docker_generator.py
│   └── compose_generator.py
│
├── templates/
│   ├── Dockerfile.j2
│   └── docker-compose.yml.j2
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Example Flask API

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(port=5000)
```

---

## Usage

Generate deployment files:

```bash
python main.py test/flask-api
```

Output:

```text
Project Detection

Framework : Flask
Entrypoint : app.py
Port       : 5000

Dockerfile generated
docker-compose.yml generated
```

---

## Generated Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

---

## Generated docker-compose.yml

```yaml
version: "3.9"

services:
  app:
    build: .

    ports:
      - "5000:5000"

    restart: unless-stopped
```

---

## Installation

Clone repository:

```bash
git clone <repository-url>

cd containerizeme
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```
