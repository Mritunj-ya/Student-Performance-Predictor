import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from src.config import (DataIngestionConfig, DataTransformationConfig)
from sklearn.compose import ColumnTransformer
from src.utils import save_object

class DataTransformation:
    def __init__(self):
        self.transformation_config=DataTransformationConfig()

    def initiate_data_transformation(self):
        print("Data Transformation Started")
        config=DataIngestionConfig()
        train_df=pd.read_csv(config.train_data_path)
        test_df=pd.read_csv(config.test_data_path)
        
        print(train_df.shape)
        print(test_df.shape)

        target_column="G3"
        X_train=train_df.drop(columns=[target_column])
        Y_train=train_df[target_column]
        X_test=test_df.drop(columns=[target_column])
        Y_test=test_df[target_column]

        print(X_train.shape)
        print(Y_train.shape)

        print(X_test.shape)
        print(Y_test.shape)

        categorical_features = [
    "school",
    "sex",
    "address",
    "famsize",
    "Pstatus",
    "Mjob",
    "Fjob",
    "reason",
    "guardian",
    "schoolsup",
    "famsup",
    "paid",
    "activities",
    "nursery",
    "higher",
    "internet",
    "romantic"
]
        preprocessor=ColumnTransformer(
            transformers=[
                (
                    "cat",
                    OneHotEncoder(handle_unknown="ignore"),
                                categorical_features
                )
            ],
            remainder="passthrough"
        )
        X_train=preprocessor.fit_transform(X_train)
        X_test=preprocessor.transform(X_test)
        save_object(
            self.transformation_config.preprocessor_obj_path,
            preprocessor
        )

        print(type(X_train))
        print(type(X_test))

        print(X_train.shape)
        print(X_test.shape)
        return(
            X_train,
            X_test,
            Y_train,
            Y_test,
            self.transformation_config.preprocessor_obj_path
        )