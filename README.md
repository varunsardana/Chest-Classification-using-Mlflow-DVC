# 🩻 Chest Cancer Classification using MLflow, DVC, Docker, and AWS

Overview. End‑to‑end deep‑learning pipeline to classify chest cancer using a transfer‑learned VGG16 model. The project is fully reproducible (DVC), tracked (MLflow on DagsHub), containerized (Docker), and deployable to AWS EC2 via GitHub Actions and a self‑hosted runner. A lightweight Flask app is included for prediction.

Disclaimer. For education only — not for clinical use.
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

```
.
├── config/ # YAML config files
├── model/ # Saved model weights / exported model
├── research/ # Notebooks & scratch experiments
├── templates/ # HTML templates (Flask UI)
├── src/
│ └── chestcancerClassifier/ # Core components (data, model, utils, pipelines)
├── .github/workflows/ # GitHub Actions (CI/CD)
├── Dockerfile # Docker build for train/serve
├── app.py # Flask app for local prediction
├── dvc.yaml # DVC pipeline config (optional)
├── mlruns/ # Local MLflow runs (if not using remote)
├── params.yaml # Hyperparameters & paths
├── config.yaml # Project paths / toggles
└── README.md
```
---

## ⚙️ ML Pipeline Overview

- Data Ingestion — download a ZIP from Google Drive (config.data_ingestion.source_URL) to artifacts/data_ingestion/data.zip, unzip to artifacts/data_ingestion/, and record the dataset snapshot with DVC.

- Prepare Base Model (VGG16) — build transfer‑learning head; optionally freeze early layers.

- Model Training — augmentation, class‑weights (if needed), callbacks; log to MLflow.

- Model Evaluation — compute metrics, confusion matrix; log artifacts to MLflow.

- Serve (optional) — Flask app for /predict and a simple upload UI.

Each stage is reproducible; reruns attach to a specific dataset snapshot via DVC.

---

## 🔁 Quickstart

Prerequisites

- Python **3.10 or 3.11** (required — TensorFlow is not compatible with Python 3.12+)
- Git
- DVC (pip install dvc + your remote extra, e.g. dvc[s3])
- Docker (optional but recommended)



1) Clone the repository

  ```bash
  git clone https://github.com/varunsardana/Chest-Classification-using-MLflow-DVC
  cd Chest-Classification-using-MLflow-DVC


2) Create and activate a virtual environment
   Option A: Conda (if installed)

   conda create -n cancerenv python=3.10 -y
   conda activate cancerenv


   Option B: venv (recommended if conda is unavailable)

   python3.10 -m venv .venv
   source .venv/bin/activate


   Install dependencies
   pip install --upgrade pip
   pip install -r requirements.txt


   Apple Silicon (M1 / M2 / M3) note

   If TensorFlow crashes on macOS, install the Apple-maintained build:
   pip uninstall -y tensorflow
   pip install tensorflow-macos
  
  
3) Pull versioned data (DVC)
   Configure your DVC remote if needed (example)
   dvc remote add -d storage s3://<bucket>/<path>
   dvc remote modify storage access_key_id ...
   dvc remote modify storage secret_access_key ...

4) Configure tracking (MLflow on DagsHub)
	
   Set these environment variables (use a token, don’t commit it):
   export MLFLOW_TRACKING_URI=https://dagshub.com/varunsardana2006/Chest-Classification-using-MLflow-DVC
   export MLFLOW_TRACKING_USERNAME=varunsardana2006
   export MLFLOW_TRACKING_PASSWORD=<YOUR_DAGSHUB_TOKEN>

5) Run the pipeline
   
   python main.py

   Or run specific stages (if exposed under src/.../pipeline), e.g.:

   python -m src.chestcancerClassifier.pipeline.stage_01_data_ingestion
   python -m src.chestcancerClassifier.pipeline.stage_02_prepare_base_model
   python -m src.chestcancerClassifier.pipeline.stage_03_model_trainer
   python -m src.chestcancerClassifier.pipeline.stage_04_model_evaluation

## 🌐 Flask App (Local Prediction)

Run a simple web app to upload an image and get a prediction:

python app.py
open http://127.0.0.1:8080 (or the port printed in your console)


## ☁️ Deployment: GitHub Actions → AWS EC2 (Self‑Hosted Runner)

This repo ships with a workflow that builds the Docker image and runs it on an EC2 instance using a self‑hosted runner installed on that instance.

One‑time EC2 setup

Launch Ubuntu EC2; open security‑group ports you need (e.g., 80/8080 for app).

Install Docker and add your user to the docker group.

Install GitHub self‑hosted runner on EC2 and run as a service:

   sudo ./svc.sh install
   sudo ./svc.sh start
    or use runsvc.sh to keep the runner alive

(Optional) Set a domain + Nginx reverse proxy; use Certbot for TLS.

CI/CD overview

On push/PR to main, GitHub Actions:

installs deps, runs tests (if present), builds Docker image

on the self‑hosted runner, restarts the container with the latest image

Keep sensitive values as GitHub Secrets or EC2 environment variables.

If your workflow requires DagsHub credentials, pass them via env: in the job from GitHub Secrets.


# 🧾 Dataset & Credits

Dataset: https://www.kaggle.com/datasets/mohamedhanyyy/chest-ctscan-images 

Acknowledgements: TensorFlow/Keras, DVC, MLflow, DagsHub, and related OSS.


# Demo Screenshot


<img width="1466" height="791" alt="Screenshot 2025-07-31 at 7 12 01 PM" src="https://github.com/user-attachments/assets/aa3bbc98-fd01-46f5-aa22-640a96d9edf5" />
