import requests

base_url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaCode'
# base_url = 'http://api.visitkorea.or.kr/openapi/service'
service_key = "gRUX5P33koKONMFfxvMtowyPSjacHjsgcJtR85r0iDBAQ20pLll2ns%2BoOzeHhKKfZ9tvSZR2RkUuzQLx1KA1YQ%3D%3D"
# service_key = service_key.encode('utf-8')

params = {
    'ServiceKey': service_key,
    'numOfRows': 10,
    'pageNo': 1,
    'MobileOS': 'ETC',
    'MobileApp' : 'DayTour',
    'areaCode' : 1,
    '_type' : 'json'

}
res = requests.get(url=base_url, params=params)
print(res.text)