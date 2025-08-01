# 🩻 Chest Cancer Classification using MLflow, DVC, Docker, and AWS

This project builds an end-to-end machine learning pipeline to classify chest cancer using deep learning with VGG16. The project includes data tracking, model training, experiment logging, and automated deployment to an AWS EC2 instance using GitHub Actions.

---

## 📌 Project Highlights

- 🔍 Deep learning model using pre-trained **VGG16**
- 🔁 End-to-end ML pipeline with **DVC**
- 📊 Experiment tracking with **MLflow** hosted on **DagsHub**
- 🐳 Containerized with **Docker**
- 🚀 CI/CD via **GitHub Actions**
- ☁️ Deployed to **AWS EC2**

---

## 🛠️ Tech Stack

| Area                     | Tools Used                            |
|--------------------------|----------------------------------------|
| Programming Language     | Python                                |
| ML/DL Framework          | TensorFlow / Keras                    |
| Data Versioning          | DVC                                   |
| Experiment Tracking      | MLflow + DagsHub                      |
| Deployment               | AWS EC2, Docker, GitHub Actions       |
| Web Interface (optional) | Flask (can be used with `app.py`)     |

---

## 📂 Project Structure


.
├── config/                         # YAML config files
├── model/                          # Saved model weights
├── research/                       # Test notebooks
├── templates/                      # HTML templates (if Flask is used)
├── src/chestcancerClassifier/     # All core components
├── .github/workflows/             # GitHub Actions CI/CD
├── Dockerfile                     # Docker setup
├── app.py                         # Flask app for prediction
├── dvc.yaml                       # DVC pipeline config
├── mlruns/                        # MLflow run logs
└── README.md                      # This file


---

## ⚙️ ML Pipeline Overview

This pipeline is organized into modular stages:

1. **Data Ingestion**
2. **Prepare Base Model (VGG16)**
3. **Model Training**
4. **Model Evaluation**
5. **Prediction with Flask (optional)**

Each stage is tracked and versioned using **DVC**.

---

## 🔁 Workflow Steps

1. `Update config.yaml` - base configurations
2. `Update params.yaml` - all hyperparameters
3. `Run training pipeline using main.py`
4. `Track experiments using MLflow`
5. `Push code & DVC data to GitHub`
6. `Deployment to AWS via GitHub Actions`

---

## 🧪 Experiment Tracking with MLflow

Tracking is integrated with [DagsHub](https://dagshub.com/varunsardana2006/Chest-Classification-using-MLflow-DVC):

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/varunsardana2006/Chest-Classification-using-MLflow-DVC
export MLFLOW_TRACKING_USERNAME=varunsardana2006
export MLFLOW_TRACKING_PASSWORD=YOUR_TOKEN


## Set Up Instructions:

Clone the repo: git clone https://github.com/varunsardana/Chest-Classification-using-MLflow-DVC
cd Chest-Classification-using-MLflow-DVC

conda create -n cancerenv python=3.10 -y
conda activate cancerenv
pip install -r requirements.txt

Pull data using DVC: dvc pull

Run pipeline: python main.py

🌐 Run Flask App Locally (optional)

To serve predictions using a web app: python app.py



## ☁️ Deployment to AWS via GitHub Actions
The GitHub Actions workflow automatically deploys the Docker container to an EC2 instance via self-hosted runner.

Steps already configured:
	•	Create EC2 instance
	•	Install Docker and self-hosted runner
	•	Run ./run.sh inside actions-runner
	•	GitHub Actions triggers deployment pipeline automatically




<img width="1468" height="803" alt="Screenshot 2025-07-31 at 7 52 07 PM" src="https://github.com/user-attachments/assets/7fedefe3-8901-4f02-9e97-96659657f8c2" />















