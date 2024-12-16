# Sentiment Analysis Web Application using Fine-Tuned BERT and LoRA
## Final project at LSML2 Course at HSE. Andreev Roman. MDS'23

This project is a **Sentiment Analysis** web application built with a fine-tuned BERT model using LoRA (Low-Rank Adaptation). It allows users to analyze the sentiment (positive or negative) of movie reviews. The application includes a backend API (FastAPI) for predictions and a simple HTML frontend with Bootstrap for user interaction.

## Features

1. **Machine Learning Model**:  
   - A fine-tuned BERT model (`bert-base-uncased`) optimized with LoRA for efficient training.  
   - Achieves **87.4% accuracy** on the IMDB dataset.  
   - Supports single and batch predictions.

2. **Backend**:  
   - Implemented with **FastAPI** for serving predictions.  
   - Supports two endpoints:
     - `/predict`: Analyze a single review.  
     - `/predict_batch`: Analyze multiple reviews in one request.  
   - CORS enabled for frontend communication.

3. **Frontend**:  
   - Simple and clean user interface created using **HTML** and **Bootstrap**.  
   - Features:
     - Dynamic input fields for multiple reviews.  
     - A loading spinner indicating processing status.  
     - Real-time display of prediction results.  

4. **Deployment**:  
   - Dockerized application for easy deployment.  
   - Managed using `docker-compose` to run both backend and frontend as separate services.

---

## Project Structure

```plaintext
project/
 ├── app.py                # FastAPI backend
 ├── saved_model/          # Directory containing the fine-tuned BERT model and tokenizer
 ├── frontend/             # Frontend HTML files
 │   └── index.html
 ├── requirements.txt      # Python dependencies
 ├── Dockerfile            # Dockerfile for building the backend API
 ├── docker-compose.yml    # Compose file for managing frontend and backend services
 ├── logs/                 # Directory for storing training and API logs
 ├── results/              # Directory for saving initial training results and checkpoints
 ├── results_improved/     # Directory for saving improved training results (e.g., with hyperparameter tuning)
 └── wandb/                # Directory automatically created by Weights & Biases for experiment tracking
```

---

## Technologies Used

### Machine Learning
- **BERT** (`bert-base-uncased`) fine-tuned on the IMDB dataset.
- **LoRA** (Low-Rank Adaptation) for efficient parameter fine-tuning.

### Backend
- **FastAPI** for high-performance API development.
- **Transformers** library (HuggingFace) for model inference.
- **PyTorch** as the deep learning framework.

### Frontend
- **HTML, CSS, Bootstrap** for a responsive and clean user interface.
- **JavaScript** for dynamic functionality (API calls, loading spinner).

### Deployment
- **Docker** for containerizing backend and frontend services.
- **Docker Compose** for orchestrating multiple services.
- **Nginx** for serving static frontend files.

### Experiment Tracking and Logging
- **Weights & Biases (W&B)** for experiment tracking, including metrics and hyperparameters.
- Logs and training results are stored in dedicated directories:
  - `logs/`
  - `results/`
  - `results_improved/`
    
<img width="1721" alt="W B1" src="https://github.com/user-attachments/assets/c697c91c-ba56-4747-bca2-b2cde05b5639" />
<img width="1723" alt="W B2" src="https://github.com/user-attachments/assets/e02005b5-4d6b-4444-bd2b-caa828497b7e" />

---

## Setup Instructions

### Prerequisites

Ensure the following software is installed on your machine:
- [**Docker**](https://docs.docker.com/get-docker/)  
- [**Docker Compose**](https://docs.docker.com/compose/install/)

### Steps to Run the Project

1. **Clone the Repository**  
   First, clone this repository to your local machine:
   ```bash
   git clone https://github.com/Andreevromano/HSE_LSML2_FP.git
   cd HSE_LSML2_FP
   ```
2. **Build and Run the Project**  
  Use (`docker-compose`) to build the Docker images and start the backend (API) and frontend services:
   ```bash
   docker-compose up --build
   ```
3. **Access the Application**  
   - Frontend: Open a browser and navigate to (`http://localhost:8080`)
   - Backend API: The API is available at (`http://localhost:8000`)
4. **Test the API**  
  You can test the API endpoints using tools like curl, Postman, or Python’s (`requests`) library.
   - Single Prediction Endpoint (`(/predict)`):
     Send a POST request with a single review:
   ```bash
   curl -X POST http://localhost:8000/predict \
   -H "Content-Type: application/json" \
   -d '{"text":"This movie is fantastic!"}'

   ```
   Response:
   
   <img width="571" alt="image" src="https://github.com/user-attachments/assets/4c820332-2f24-4b26-beec-a2e46812fe5f" />

   - Batch Prediction Endpoint (`(/predict)`):
     Send a POST request with multiple reviews:
   ```bash
   curl -X POST http://localhost:8000/predict_batch \
   -H "Content-Type: application/json" \
   -d '{"texts": ["This movie was amazing!", "Bad actors and movie!"]}'


   ```
   Response:

   <img width="566" alt="image" src="https://github.com/user-attachments/assets/42d95ebb-eea3-40e0-b008-7d44dd775164" />



---

## Results

### Result in Notebook

<img width="1000" alt="Result in Notebook" src="https://github.com/user-attachments/assets/3a6a02de-a9b0-408a-9ef0-39875fe71906" />

### Result in Frontend

<img width="1720" alt="Result in Frontend" src="https://github.com/user-attachments/assets/c1055e00-e86d-4168-927e-a5bf548d4a1a" />

