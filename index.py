from flask import Flask, request, render_template
from weather import seven_days_forecast
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index(city='no_city', res_dict={}):
    bgcolor = os.environ['BG_COLOR']
    if request.method == 'GET':
        city = request.args.get('city')
        res_dict = seven_days_forecast(city) if city else {}
    return render_template('weather.html', city=city, resdict=res_dict, bgcolor=bgcolor)

with open("./history/searchHistory.txt","r+") as file:
        f = file.read()
        
@app.route('/history', methods=['GET'])
def history():
    return render_template('history.html', r=f)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
