from flask import Flask,render_template,request
import requests
import pickle

import sklearn

app = Flask(__name__)

model = pickle.load(open('rf_model.pkl', 'rb'))


@app.route('/',methods=['GET'])
def Home():
    return render_template('DaibetiesPrediction.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        Pregnancy = int(request.form['Pregnancy'])
        Glucose = int(request.form['Glucose'])
        BloodPressure = int(request.form['BloodPressure'])
        SkinThickness = int(request.form['SkinThickness'])
        Insulin = int(request.form['Insulin'])
        BMI = float(request.form["BMI"])
        DiabetesPedigreeFunction=float(request.form["DiabetesPedigreeFunction"])
        Age =  int(request.form["Age"])
    
    
        outcome = model.predict([[Pregnancy,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
       
        if outcome==0:
            return render_template('DaibetiesPrediction.html', prediction_texts="You do not have Diabeties")
        else:
            return render_template("DaibetiesPrediction.html",  prediction_texts="You have Diabeties")
    
    
      
    
if __name__=="__main__":
   app.run(debug=True)


   
