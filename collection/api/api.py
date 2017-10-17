from urllib.parse import urlencode

from .json_request import json_request

SERVICE_KEY = '%2FfZdR%2Bue1CSxLEnMkZXa9iDYontLTMTIteD5%2BzYCiMYpDKUZNUh2FHGDQ04zazSEmLl34FClDQk8a7flFCIQKA%3D%3D'


def pd_gen_url(endpoint, **params):
    return '%s?%s&serviceKey=%s' % (endpoint, urlencode(params), SERVICE_KEY)


def pd_fetch_tourspot_visitor(
        district1='',
        district2='',
        tourspot='',
        year=0,
        month=0):

    endpoint = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
    pageno = 1

    url = pd_gen_url(
        endpoint,
        YM='{0:04d}{1:02d}'.format(year, month),
        SIDO=district1,
        GUNGU=district2,
        RES_NM=tourspot,
        numOfRows=100,
        _type='json',
        pageNo=pageno)
    json_result = json_request(url=url)
    print(json_result)
