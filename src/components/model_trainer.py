from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from src.config import ModelTrainerConfig
from src.utils import save_object

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
    def initiate_model_trainer(
            self,
            X_train,
            Y_train,
            X_test,
            Y_test
    ):
        print("Model Training Started")
        model=RandomForestRegressor(
            random_state=42
        )
        model.fit(X_train,Y_train)
        pred=model.predict(X_test)

        mae=mean_absolute_error(Y_test,pred)
        rmse=mean_squared_error(Y_test,pred)**0.5
        r2=r2_score(Y_test,pred)

        print("MAE:", mae)
        print("RMSE:", rmse)
        print("R2 Score:", r2)

        save_object(
            self.model_trainer_config.model_obj_path,
            model
        )
        print("Model Training Completed")
        return r2