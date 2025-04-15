# 🛡️ Network Security Threat Detection - End-to-End MLOps Project

This project is a full-scale **Machine Learning pipeline for detecting phishing attacks** using structured network traffic data. It was developed following MLOps principles, including proper modularization, validation, artifact tracking, experiment tracking with MLflow, CI/CD with GitHub Actions, and deployment with Docker + AWS EC2.

Inspired by the course **"End To End MLOPS Projects With ETL Pipelines - Building Network Security System"**, this solution handles everything from ingestion to batch prediction and model monitoring.

---

## 🎯 Objective

To build and productionize a machine learning system that detects malicious or phishing-based network activity using automated pipelines, model versioning, and deployment best practices.

---

## 🔧 Features

- ✅ Data Ingestion from Phishing Dataset  
- ✅ Schema-based Validation with Drift Detection  
- ✅ Data Transformation with preprocessing pipeline  
- ✅ Model Training with hyperparameter tuning  
- ✅ MLFlow Tracking and Experiment Logging  
- ✅ Batch Prediction Pipeline  
- ✅ Docker + GitHub Actions for CI/CD  
- ✅ AWS S3 Storage & EC2 Deployment  
- ✅ REST API via FastAPI  

---

## 📚 Based On Course Sections

| Course Topic                                   | Implemented |
|-----------------------------------------------|-------------|
| Project Structure & Environment Setup          | ✅          |
| GitHub Repo Setup                              | ✅          |
| Packaging the Project                          | ✅          |
| Logging & Exception Handling                   | ✅          |
| Intro to ETL Pipelines                         | ✅          |
| MongoDB Atlas Setup                            | ✅          |
| ETL Pipeline Setup with Python                 | ✅          |
| Data Ingestion Architecture                    | ✅          |
| Data Ingestion & Configuration                 | ✅          |
| Data Validation (Schema & Drift)               | ✅          |
| Data Transformation Architecture & Code        | ✅          |
| Model Training                                 | ✅          |
| Model Evaluation with Hyperparameter Tuning    | ✅          |
| MLFlow Integration                             | ✅          |
| MLFlow Tracking with DagsHub                   | ✅          |
| Model Pusher Module                            | ✅          |
| Batch Prediction Pipeline                      | ✅          |
| Upload Artifacts to S3                         | ✅          |
| Docker Image Build + GitHub Actions            | ✅          |
| Docker Push + EC2 Deployment                   | ✅          |

---

## 🗂️ Project Structure

```
networksecurity/
├── app.py                         # FastAPI app for inference
├── main.py                        # Pipeline launcher
├── push_data.py                   # Push local data to MongoDB
├── setup.py                       # Package setup
├── Dockerfile                     # Docker container setup
├── .github/workflows/main.yml     # GitHub Actions CI workflow
├── Network_Data/                  # Raw dataset
├── Artifacts/                     # Generated pipeline artifacts
├── data_schema/schema.yaml        # Schema for data validation
├── final_model/                   # Final model + preprocessor
├── templates/                     # FastAPI HTML templates
├── networksecurity/               # Core ML package
│   ├── components/                # Ingestion, transformation, training
│   ├── pipeline/                  # Training + batch prediction
│   ├── entity/                    # Config and artifact data classes
│   ├── cloud/                     # S3 sync logic
│   ├── utils/                     # Utility functions
│   ├── logging/, exception/       # Custom logger and error handling
└── requirements.txt
```


## ☁️ CI/CD and Deployment

- Artifacts pushed to **AWS S3**  
- CI/CD via **GitHub Actions**  
- Deployed on **AWS EC2 Instance**

---

## 🧪 ML Tracking

- **MLFlow** for experiment tracking and logging  
- **DagsHub** integration for remote MLFlow UI

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file.

---

## 👨‍💻 Author

Jeevan Aher
Master’s Student, Computer Science
University of Illinois Springfield  
[LinkedIn](https://www.linkedin.com/in/jeevanaher732)
