import os
import pandas as pd 
from sklearn.model_selection import train_test_split
from src.utils import save_object
from src.config import DataIngestionConfig

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    def initiate_data_ingestion(self):
        print("Data Ingestion Started")
        df=pd.read_csv("data/student+performance/student/student-mat.csv",
        sep=";")
        os.makedirs("artifacts",exist_ok=True)
        df.to_csv(self.ingestion_config.raw_data_path,index=False)
        train_set, test_set=train_test_split(
            df,
            test_size=0.2,
            random_state=42
            )
        train_set.to_csv(self.ingestion_config.train_data_path,index=False)
        test_set.to_csv(self.ingestion_config.test_data_path,index=False)
        print("Data Ingestion Completed")

        return(self.ingestion_config.train_data_path,
               self.ingestion_config.test_data_path)
    
        
        

