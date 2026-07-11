from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

ingestion=DataIngestion()
ingestion.initiate_data_ingestion()

transformation=DataTransformation()
X_train, X_test,Y_train,Y_test,preprocessor_path=(
transformation.initiate_data_transformation())

trainer=ModelTrainer()
trainer.initiate_model_trainer(
    X_train,
    Y_train,
    X_test,
    Y_test
)

