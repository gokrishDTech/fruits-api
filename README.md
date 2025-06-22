# 🍎 Fruits API

A simple, beginner-friendly **FastAPI** microservice to manage a list of fruits.

---

## 📌 Features & Endpoints

- `GET /fruits` → List all fruits  
- `GET /fruits/{id}` → Get a specific fruit by ID  
- `POST /fruits` → Add a fruit  
  Example JSON:  
  ```json
  {
    "fruit": "apple",
    "color": "red"
  }
  ```

---

## 🚀 Run the App Locally (Development)

Make sure your virtual environment is activated:

```bash
uvicorn app.main:app --reload
```

---

## 🧪 Run Tests

```bash
PYTHONPATH=. pytest
```

---

## 🐳 Build & Run with Docker

### 1️⃣ Install Docker (if not already installed)

```bash
sudo apt install docker.io -y
sudo usermod -aG docker $USER
newgrp docker
```

### 2️⃣ Build and Run the Docker Container

```bash
docker build -t fruits-api .
docker run -p 8000:8000 fruits-api
```

---

## 🔁 CI/CD with GitHub Actions

- **CI Workflow**: Automatically runs tests and builds/pushes a Docker image to DockerHub
- **CD Workflow**: Deploys the image to a live environment using a self-hosted GitHub Actions runner

---

## 🌐 Public Access (For Cloud VM like EC2)

If you're deploying to a cloud server:

- ✅ Make sure **port 8000** is open in your EC2 Security Group or firewall
- 🌍 Access your API in browser or Postman at:

```
http://<YOUR_PUBLIC_IP>:8000/fruits
```

---

## ✅ Done!

Your Fruits API is now ready for development, testing, Dockerization, and CI/CD automation.
