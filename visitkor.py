import requests

base_url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/detailCommon'
# base_url = 'http://api.visitkorea.or.kr/openapi/service'
service_key = "uyhEtW8fzsb3e9mz1%2BDoRmdabPTkWTLFRaTUE5Sq4yGK7r7Rm1ZGbSIujcoc96reP5k8YlYKdasBpWbHuSlG0g%3D%3D"
service_key = service_key.encode('utf-8')

params = {
    'ServiceKey': service_key,
    'numOfRows': '10',
    'pageNo': '1',
    'MobileOS': 'ETC',
    'MobileApp' : 'AppTest',
    'areaCode' : 1,
    '_type' : 'json'

}
res = requests.get(url=base_url, params=params)
print(res.text)