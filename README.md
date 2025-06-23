# Microservice-based-AI-Image-Captioning-Web-App

# 🖼️ AI Image Captioning Web App

A microservice-based AI web application that generates natural language captions from uploaded images using deep learning models. Built using **Flask** for the frontend/orchestration and **FastAPI** as a microservice to serve a **pretrained image captioning model (BLIP)**.

![Demo](https://img.shields.io/badge/Status-Working-green) ![Python](https://img.shields.io/badge/Python-3.8+-blue)

--- Features
- Upload an image via a simple web interface
- Generate human-like captions using the **BLIP image captioning model**
- Microservice architecture (Flask <-> FastAPI)
- Stores caption history in a **SQLite database**
- REST API communication between services

--- Tech Stack

| Layer     | Tech                 |
|-----------|----------------------|
| Frontend  | HTML, Jinja2 (Flask) |
| Backend   | Flask + FastAPI      |
| ML Model  | BLIP (HuggingFace)   |
| Storage   | SQLite               |


Go to: http://localhost:5000
Upload an image → Get a caption 
See caption history at: /history
