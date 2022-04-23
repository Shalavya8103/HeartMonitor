import numpy
from flask import Flask, render_template, request, redirect, url_for, flash
import pickle

app = Flask(__name__)

model = pickle.load(open('venv\m.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    ytest=[]
    BMI=request.form['BMI']
    ytest.append(float(BMI))
    print(ytest)
    
    phy=request.form['PhysicalHealth']
    ytest.append(float(phy))

    phy=request.form['MentalHealth']
    ytest.append(float(phy))

    slptme=request.form['SleepTime']
    ytest.append(float(slptme))

    Smoking=request.form['Smoking']
    sl=[0,0]
    if Smoking=='0':
        sl[0]=1
    else:
        sl[1]=1
    for i in sl:
        ytest.append(i)


    AlcoholDrinking=request.form['AlcoholDrinking']
    ad=[0,0]
    if AlcoholDrinking=='0':
        ad[0]=1
    else:
        ad[1]=1
    for i in ad:
        ytest.append(i)

    Stroke=request.form['Stroke']
    st=[0,0]
    if Stroke=='0':
        st[0]=1
    else:
        st[1]=1
    for i in st:
        ytest.append(i)

    DiffWalking=request.form['DiffWalking']
    dw=[0,0]
    if DiffWalking=='0':
        dw[0]=1
    else:
        dw[1]=1
    for i in dw:
        ytest.append(i)

    Sex=request.form['Sex']
    sx=[0,0]
    if Sex=='1':
        sx[0]=1
    else:
        sx[1]=1
    for i in sx:
        ytest.append(i)

    AgeCategory=request.form['AgeCategory']
    al=[0,0,0,0,0,0,0,0,0,0,0,0,0]
    al[int(AgeCategory)]=1
    for i in al:
        ytest.append(i)
        
    Race=request.form['Race']
    ra=[0,0,0,0,0,0]
    ra[int(Race)]=1
    for i in ra:
        ytest.append(i)

    Diabetic=request.form['Diabetic']
    db=[0,0,0,0]
    db[int(Diabetic)]=1
    for i in db:
        ytest.append(i)
    
    PhysicalActivity=request.form['PhysicalActivity']
    pa=[0,0]
    if PhysicalActivity=='1':
        pa[0]=1
    else:
        pa[1]=1
    for i in pa:
        ytest.append(i)

    GenHealth=request.form['GenHealth']
    gh=[0,0,0,0,0]
    gh[int(GenHealth)]=1
    for i in gh:
        ytest.append(i)
    
    Asthma=request.form['Asthma']
    ast=[0,0]
    if Asthma=='0':
        ast[0]=1
    else:
        ast[1]=1
    for i in ast:
        ytest.append(i)
    
    KidneyDisease=request.form['KidneyDisease']
    kd=[0,0]
    if KidneyDisease=='0':
        kd[0]=1
    else:
        kd[1]=1
    for i in kd:
        ytest.append(i)
    
    SkinCancer=request.form['SkinCancer']
    sc=[0,0]
    if SkinCancer=='0':
        sc[0]=1
    else:
        sc[1]=1
    for i in sc:
        ytest.append(i)
    feat_list =[ytest]
    print("\n",feat_list)
    prediction = model.predict(feat_list)
    out  = prediction[0]
    print(out)
    if out == 0:
        text = "Yes"
    else:
        text = "No"
    return render_template('index.html', prediction_text='Does the person has hear Disease? {}'.format(text))

if __name__ == '__main__':
    app.run(debug=True)