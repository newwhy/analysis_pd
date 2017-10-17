import analysis_pd.collection.api as pdapi

# test for ps_gen_url
"""
url = pdapi.pd_gen_url(
    "http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList",
    YM='{0:04d}{1:02d}'.format(2017, 1),
    SIDO='서울특별시',
    GUNGU='',
    RES_NM='',
    numOfRows=100,
    _type='json',
    pageNo=2)
print(url)
"""
# test from pd_fetch_tourspot_visitor
pdapi.pd_fetch_tourspot_visitor(district1='서울특별시', year=2017, month=1)

