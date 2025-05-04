# MLflow Tracking with Docker Compose

This project demonstrates how to set up MLflow tracking server with Docker Compose for machine learning experiment tracking.

## Project Structure

```
.
├── docker-compose.yml        # Docker Compose configuration
├── train.py                  # Training script with MLflow tracking
├── mlflow.db                 # SQLite database for MLflow (created after first run)
├── artifacts/                # Directory for storing model artifacts
└── README.md                 # This file
```

## Prerequisites

- Docker
- Docker Compose

## Quick Start

### 1. Start the MLflow Server and Training Job

Run the following command to start both the MLflow tracking server and the training job:

```bash
docker-compose up --build
```

This will:
1. Start the MLflow tracking server on port 5000
2. Run the training job which will log experiments to the tracking server

### 2. Access the MLflow UI

After starting the services, you can access the MLflow tracking UI at:

```
http://localhost:5000
```

In the UI you'll see:
- The "Iris_Classification" experiment
- The run with logged parameters and metrics
- The trained model artifact

## How It Works

### MLflow Tracking Server

The MLflow server is configured with:
- SQLite backend store (`mlflow.db`)
- Local artifact storage (`./artifacts`)
- Accessible at `http://localhost:5000`

### Training Job

The training job:
1. Loads the Iris dataset
2. Trains a RandomForestClassifier
3. Logs to MLflow:
   - Parameters (n_estimators)
   - Metrics (accuracy)
   - Model artifact

## Customizing

### To run just the MLflow server:

```bash
docker-compose up mlflow-server
```

### To run just the training job (after MLflow server is running):

```bash
docker-compose up training-job
```

## Troubleshooting

If you encounter connection issues:
1. Make sure the MLflow server is running first
2. Check that the training job is using the correct tracking URI (`http://mlflow-server:5000`)

## Cleaning Up

To stop and remove all containers:

```bash
docker-compose down
```

To also remove the database and artifacts:

```bash
docker-compose down -v
rm -rf artifacts/ mlflow.db
```

> **Note:** The `docker-compose.yml` file uses a Python image to run MLflow server for simplicity. In production, you might want to use an official MLflow Docker image or build a custom image.
