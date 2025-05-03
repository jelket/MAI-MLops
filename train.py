import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def train():
    try:
        mlflow.set_tracking_uri("http://localhost:5000")
        logger.info("Успешно подключено к MLflow")
    except Exception as e:
        logger.error(f"Ошибка подключения: {e}")
        raise

    # Загрузка данных
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

    # Настройка MLflow
    mlflow.set_tracking_uri("http://mlflow-server:5000")  # URL сервера MLflow
    mlflow.set_experiment("Iris_Classification")

    with mlflow.start_run():
        # Обучение модели
        model = RandomForestClassifier(n_estimators=100)
        model.fit(X_train, y_train)
        accuracy = model.score(X_test, y_test)

        # Логирование параметров и метрик
        mlflow.log_param("n_estimators", 100)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.sklearn.log_model(model, "iris_model")

if __name__ == "__main__":
    train()