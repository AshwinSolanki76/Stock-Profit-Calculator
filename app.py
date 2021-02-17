from datetime import datetime,date
from flask import Flask, render_template, request,url_for
from Stock import GetDetail
import numpy
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
        PriceThen,PriceNow=GetDetail(datee,d['StockName'],d['Capital'])
        name['Profit']=int((numpy.float32(d['Capital'])/PriceThen)*PriceNow-numpy.float32(d['Capital']))
        name['PriceThen']=PriceThen
        name['DateThen']=datee
        name['DateNow']=date.today()
        name['PriceNow']=PriceNow
        name['Growth']=int((PriceNow-PriceThen)*100/PriceThen)
        print("done")
        return render_template("result.html",result =name)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run(debug = True)