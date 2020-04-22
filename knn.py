import flask
from flask import Flask, send_file, escape, request
from io import BytesIO
import pandas as pd
import pickle
import numpy as np
import joblib

#json =  'D:\Predicting-WalmartSales\graficos.json'


fname = 'model/model_knn.pkl'
model = joblib.load(open(fname, 'rb'))

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return flask.render_template('main.html')
    
    if flask.request.method == 'POST':
        user_inputs = {
            'Genero': flask.request.form['Genero'],
            'Idade': flask.request.form['Idade'],
            'RendaAnual': flask.request.form['RendaAnual'],
            'Pontuacao': flask.request.form['Pontuacao'],
        }

        df = pd.DataFrame(index=[0], columns=['Genero', 'Idade', 'RendaAnual', 'Pontuacao'])

        for i in user_inputs.items():
            df[i[0]] = i[1]
        
        cols = ['Genero','Idade', 'RendaAnual', 'Pontuacao']
        #Tratando os dados
        for col in cols:  
	        df[col] = pd.to_numeric(df[col])
            
        df = df.fillna(1)

        y_pred = model.predict(df)[0]
        df['pred'] = y_pred
        print(y_pred)

        return flask.render_template('main.html', y_pred = y_pred)
        
if __name__ == '__main__':
    app.run() #host='0.0.0.0', debug=True 