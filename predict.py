import mlflow
import numpy as np
from sklearn.datasets import load_iris


def predict():
    mlflow.set_tracking_uri("http://localhost:5000")

    model_uri = "models:/Iris_Classification/latest"
    model = mlflow.sklearn.load_model(model_uri)

    input_data = np.array([[5.1, 3.5, 1.4, 0.2]])
    prediction = model.predict(input_data)

    iris = load_iris()
    target_names = iris.target_names
    print(f"Предсказанный класс: {target_names[prediction[0]]}")


if __name__ == "__main__":
    predict()