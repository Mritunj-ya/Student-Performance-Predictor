from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import predictPipeline,CustomData 
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method=="GET":
        return render_template("index.html")
    else:
        data = CustomData(
            school=request.form.get("school"),
            sex=request.form.get("sex"),
            age=int(request.form.get("age")),
            address=request.form.get("address"),
            famsize=request.form.get("famsize"),
            Pstatus=request.form.get("Pstatus"),
            Medu=int(request.form.get("Medu")),
            Fedu=int(request.form.get("Fedu")),
            Mjob=request.form.get("Mjob"),
            Fjob=request.form.get("Fjob"),
            reason=request.form.get("reason"),
            guardian=request.form.get("guardian"),
            traveltime=int(request.form.get("traveltime")),
            studytime=int(request.form.get("studytime")),
            failures=int(request.form.get("failures")),
            schoolsup=request.form.get("schoolsup"),
            famsup=request.form.get("famsup"),
            paid=request.form.get("paid"),
            activities=request.form.get("activities"),
            nursery=request.form.get("nursery"),
            higher=request.form.get("higher"),
            internet=request.form.get("internet"),
            romantic=request.form.get("romantic"),
            famrel=int(request.form.get("famrel")),
            freetime=int(request.form.get("freetime")),
            goout=int(request.form.get("goout")),
            Dalc=int(request.form.get("Dalc")),
            Walc=int(request.form.get("Walc")),
            health=int(request.form.get("health")),
            absences=int(request.form.get("absences")),
            G1=int(request.form.get("G1")),
            G2=int(request.form.get("G2"))
        )
        pred_df=data.get_data_as_dataframe()
        predict_pipeline=predictPipeline()
        result=predict_pipeline.predict(pred_df)
        return render_template(
            "index.html",
            prediction=result[0]
        )

if __name__=="__main__":
    app.run(host="0.0.0.0",port="5000",debug=True)
