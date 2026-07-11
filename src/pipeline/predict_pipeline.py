import pandas as pd
import joblib
class predictPipeline:
    def __init__(self):
        self.preprocessor=joblib.load("artifacts/preprocessor.pkl")
        self.model=joblib.load("artifacts/model.pkl")
    def predict(self,features):
        transformed_data=self.preprocessor.transform(features)
        prediction=self.model.predict(transformed_data)
        return prediction
    # We use transform() because the preprocessor has already learned the encoding during training. During prediction, we only apply the same transformation to new input data. Using fit_transform() would make the preprocessor learn again from the new data, which would change the feature mapping and make it inconsistent with the model.
class CustomData:
    def __init__(
        self,
        school,
        sex,
        age,
        address,
        famsize,
        Pstatus,
        Medu,
        Fedu,
        Mjob,
        Fjob,
        reason,
        guardian,
        traveltime,
        studytime,
        failures,
        schoolsup,
        famsup,
        paid,
        activities,
        nursery,
        higher,
        internet,
        romantic,
        famrel,
        freetime,
        goout,
        Dalc,
        Walc,
        health,
        absences,
        G1,
        G2
    ):

        self.school = school
        self.sex = sex
        self.age = age
        self.address = address
        self.famsize = famsize
        self.Pstatus = Pstatus
        self.Medu = Medu
        self.Fedu = Fedu
        self.Mjob = Mjob
        self.Fjob = Fjob
        self.reason = reason
        self.guardian = guardian
        self.traveltime = traveltime
        self.studytime = studytime
        self.failures = failures
        self.schoolsup = schoolsup
        self.famsup = famsup
        self.paid = paid
        self.activities = activities
        self.nursery = nursery
        self.higher = higher
        self.internet = internet
        self.romantic = romantic
        self.famrel = famrel
        self.freetime = freetime
        self.goout = goout
        self.Dalc = Dalc
        self.Walc = Walc
        self.health = health
        self.absences = absences
        self.G1 = G1
        self.G2 = G2

    def get_data_as_dataframe(self):

        data = {
            "school": [self.school],
            "sex": [self.sex],
            "age": [self.age],
            "address": [self.address],
            "famsize": [self.famsize],
            "Pstatus": [self.Pstatus],
            "Medu": [self.Medu],
            "Fedu": [self.Fedu],
            "Mjob": [self.Mjob],
            "Fjob": [self.Fjob],
            "reason": [self.reason],
            "guardian": [self.guardian],
            "traveltime": [self.traveltime],
            "studytime": [self.studytime],
            "failures": [self.failures],
            "schoolsup": [self.schoolsup],
            "famsup": [self.famsup],
            "paid": [self.paid],
            "activities": [self.activities],
            "nursery": [self.nursery],
            "higher": [self.higher],
            "internet": [self.internet],
            "romantic": [self.romantic],
            "famrel": [self.famrel],
            "freetime": [self.freetime],
            "goout": [self.goout],
            "Dalc": [self.Dalc],
            "Walc": [self.Walc],
            "health": [self.health],
            "absences": [self.absences],
            "G1": [self.G1],
            "G2": [self.G2]
        }

        df=pd.DataFrame(data)
        return df

