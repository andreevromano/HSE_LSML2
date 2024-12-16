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

[W&B1.png](https://github.com/andreevromano/HSE_LSML2_FP/blob/e73868a4f934f389a9ff808dedbfd3adbf205a71/W%26B1.png)
![alt text]([http://url/to/img.png](https://github.com/andreevromano/HSE_LSML2_FP/blob/e73868a4f934f389a9ff808dedbfd3adbf205a71/W%26B1.png))
