# DentAI

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&style=flat-square)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow&style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-✔️-green?logo=fastapi&style=flat-square)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-✔️-blue?logo=postgresql&style=flat-square)
![License](https://img.shields.io/badge/License-MIT-informational?style=flat-square)
![Docker](https://img.shields.io/badge/Docker-✔️-blue?logo=docker&style=flat-square)

**Project Repository**: [DentAI](https://github.com/EF361/DentAI)  

## Executive Summary  
DentAI is a machine learning-powered decision-support system aimed at assisting dental professionals in identifying anomalies in radiological images. This API-first platform prioritizes ethical AI principles, reproducibility, and extensive validation to ensure safe integration into dental practice workflows.

_⚠️ Note: This project is in the **conceptual/early development stage**, and clinical claims are **not valid** at this time. Visit future releases for production-grade features._

---

## Key Features  
- **Inference API**: A FastAPI-driven RESTful API for real-time image classification and anomaly detection.  
- **Model Governance & Auditability**: Tracks model versioning, hyperparameters, and evaluation datasets for complete reproducibility.  
- **Drift & Bias Detection**: Monitors input data distribution changes, flagging potential biases over time.  
- **Security & Privacy Compliance**: Implements strict de-identification of patient data and secure image storage with encryption.  
- **Observability & Monitoring**: Integrated with Prometheus and Grafana dashboards for system health tracking.  
- **Testable Codebase**: Unit tests written with Pytest and structured for high coverage and easy debugging.  
- **Extensibility**: Dockerized microservices for easy deployment and scaling.  

---

## Architecture & Workflow  

```mermaid
graph TD
    A[Input: Dental Radiograph] -->|Image Uploaded to API| B[FastAPI Endpoint]
    B --> C[Preprocessing Pipeline]
    C --> D[TensorFlow Model Inference]
    D -->|Prediction and Uncertainty| E[Response to Client]
    E --> F[Audit Storage: Results & Metadata]
    E --> G[Monitoring: Performance Metrics (Prometheus/Grafana)]
    F --> H[Drift Detection for Bias Monitoring]
```

---

## Tech Stack & Tools  

| **Layer**                      | **Technology**         | **Purpose**                                          |
|--------------------------------|------------------------|-----------------------------------------------------|
| **Programming Language**       | Python 3.9+            | Development of backend API, preprocessing, and ML   |
| **Framework**                  | TensorFlow 2           | Machine learning model training and inference       |
| **Web Framework**              | FastAPI                | Lightweight asynchronous API endpoints              |
| **Database**                   | PostgreSQL             | Metadata storage (e.g., images, predictions, logs)  |
| **Containerization**           | Docker                 | Deployment and environment consistency              |
| **Monitoring**                 | Prometheus & Grafana   | Performance and error diagnostics                   |
| **Testing**                    | Pytest                 | Robust unit and integration testing pipeline        |

---

## Quickstart  

Follow the steps below to set up the DentAI development environment locally:

### Prerequisites:  
- **Python** 3.9 or higher  
- **Docker** (if running via containerization)  

### 1. Clone the Repository  
```bash
git clone https://github.com/EF361/DentAI.git
cd DentAI
```

### 2. Create a Python Virtual Environment  
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4. Set Up Docker (Optional)  
Build and run a Docker container for the application:  
```bash
docker build -t dentai .
docker run -dp 8000:8000 dentai
```

### 5. Run the Application Locally  
Run the development server:  
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be live at `http://127.0.0.1:8000`.

---

## Implementation Status  

| **Feature**                       | **Status**           | **Notes**                                                                 |
|-----------------------------------|----------------------|---------------------------------------------------------------------------|
| Dental Image Upload               | ✅ Implemented       | Accepts radiographs via FastAPI endpoints.                               |
| Model Training & Deployment       | ⚠️ Conceptual        | Placeholder model provided for testing purposes only.                    |
| Security & Compliance Controls    | ⚠️ Conceptual        | To implement de-identification, encryption, and healthcare threat model. |
| Monitoring & Observability        | ⚠️ Conceptual        | Initial Grafana/Prometheus integration planned.                          |
| Bias/Drift Detection              | ⚠️ Conceptual        | Targeted for future development.                                         |

---

## Responsible AI Model Card  

### Dataset Provenance  
- **Dataset Source**: Placeholder synthetic dataset used during concept phase. Transition to clinically validated datasets required.  
- **License & Permissions**: TBD on final dataset selection.  

### Data Composition  
- **Cohort**: To include representative dental radiographs from diverse populations.  
- **Labeling Protocol**: Manual annotations by certified radiologists planned.  

### Validation Measures  
- **Cross Validation**: To mitigate leaks; separation between training and test data enforced.  
- **Metrics**: Future releases will measure externally validated sensitivity, specificity, and subgroup fairness.  

### Intended Use  
- **Purpose**: Supplement dental professionals in examining radiographs.  
- **Contraindications**: Not for direct diagnostic conclusions or primary care use without oversight.  

---

📜 **License**  
This repository is licensed under the [MIT License](./LICENSE).  

🌟 **Contributions Welcome**  
For feedback and contributions, open an issue or submit a pull request.