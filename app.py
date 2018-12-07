# -- coding: utf-8 --

from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome DayTour data center'


@app.route('/search_area', methods=['POST'])
def search_area():
    # Request
    import requests
    import config
    base_url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaCode'
    params = {
        'ServiceKey': config.service_key,
        'numOfRows': request.form['rows'],
        'pageNo': request.form['page'],
        'MobileOS': 'ETC',
        'MobileApp': 'DayTour',
        '_type': 'json'
    }
    res = requests.get(url=base_url, params=params)

    # Data Parsing
    data = json.loads(res.text)
    data = json.dumps(data['response']['body']['items']['item'])
    return data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')