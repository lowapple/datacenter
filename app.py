# -- coding: utf-8 --

from flask import Flask, request
import json
from bson.json_util import dumps
import database
import utils

app = Flask(__name__)

@app.route('/search_area', methods=['POST'])
def search_area():
    db = database.getDatabase()
    korea_area = db.korea_area
    datas = korea_area.find()
    print(datas)
    return dumps(datas)


async def init_app():
    await init_korea_area()

async def init_korea_area():

    print('-------------- Init Korea Area --------------')

    import aiohttp
    import config

    base_url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaCode'
    params = {
        'ServiceKey': config.service_key,
        'numOfRows': 20,
        'pageNo': 1,
        'MobileOS': 'ETC',
        'MobileApp': 'DayTour',
        '_type': 'json'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url=base_url, params=params) as res:
            datas = await res.text()
            datas = json.loads(datas)
            datas = datas['response']['body']['items']['item']
            
            db = database.getDatabase()
            korea_area = db.korea_area
            # pprint.pprint(korea_area.find_one())
            # 있는지 없는지 검사한다.
            # print(korea_area.finds())
            for data in datas:
                print(data)
                if korea_area.find_one({'rnum' : data['rnum']}) == None:
                    print('insert ' + str(data))
                    korea_area.insert(data)



if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_app())
    
    app.run(debug=True, host='0.0.0.0')