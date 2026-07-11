import os
from dataclasses import dataclass
@dataclass
class DataIngestionConfig:
    raw_data_path=os.path.join("artifacts","raw.csv")
    train_data_path=os.path.join("artifacts","train.csv")
    test_data_path=os.path.join("artifacts","test.csv")

@dataclass
class DataTransformationConfig:
    preprocessor_obj_path=os.path.join(
        "artifacts",
        "preprocessor.pkl"
    )
    # preprocessor.pkl stores the preprocessing pipeline
    # Stores the fitted preprocessing steps (OneHotEncoder, ColumnTransformer, etc.) so new data is transformed in exactly the same way as the training data.
@dataclass
class ModelTrainerConfig:
    model_obj_path=os.path.join(
        "artifacts",
        "model.pkl"
    )
    # model.pkl stores the trained machine learning model
    # model.pkl stores the trained Random Forest model. It contains the learned patterns (parameters) from the training data, so we don't have to train the model again every time we want to make a prediction."