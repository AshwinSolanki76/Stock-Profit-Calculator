from datetime import datetime
from flask import Flask, render_template, request
from Stock import GetDetail
import os

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
        name={}
        for key, value in request.form.items():
            name[ key ] = value
         
        result = request.form
        d=result.to_dict(flat=False)
        datee=datetime(*[int(i) for i in d['Date'][0].split('-')])
        k=GetDetail(datee,d['StockName'],d['Capital'])
        name['Profit']=GetDetail(datee,d['StockName'],d['Capital'])
        return render_template("result.html",result =name)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run(debug = True)