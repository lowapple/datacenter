import requests
import config

base_url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaCode'

# {"items":{"item":[{"code":1,"name":"서울","rnum":1},{"code":2,"name":"인천","rnum":2},{"code":3,"name":"대전","rnum":3},{"code":4,"name":"대구","rnum":4},{"code":5,"name":"광주","rnum":5},{"code":6,"name":"부산","rnum":6},{"code":7,"name":"울산","rnum":7},{"code":8,"name":"세종특별자치시","rnum":8},{"code":31,"name":"경기도","rnum":9},{"code":32,"name":"강원도","rnum":10}]},"numOfRows":10,"pageNo":1,"totalCount":17}}}
# {"items":{"item":[{"code":1,"name":"대덕구","rnum":1},{"code":2,"name":"동구","rnum":2},{"code":3,"name":"서구","rnum":3},{"code":4,"name":"유성구","rnum":4},{"code":5,"name":"중구","rnum":5}]},"numOfRows":10,"pageNo":1,"totalCount":5}}}


params = {
    'ServiceKey': config.service_key,
    'numOfRows': 10,
    'pageNo': 1,
    'MobileOS': 'ETC',
    'MobileApp' : 'DayTour',
    'areaCode' : 3,
    '_type' : 'json'

}
res = requests.get(url=base_url, params=params)
print(res.text)
