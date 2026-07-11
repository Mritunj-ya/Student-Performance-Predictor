import os
import joblib
def save_object(file_path,obj):
    dir_path=os.path.dirname(file_path)
    os.makedirs(dir_path,exist_ok=True)
    print("Saving object to:",file_path)
    joblib.dump(obj,file_path)
    print("object saved successfully")


