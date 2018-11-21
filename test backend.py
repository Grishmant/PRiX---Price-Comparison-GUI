import requests
import json

api_key = '5YoVtLHoCqewYcyy1LG2syeBxORhyK4wd1s'
search_input = str(input('Enter keywords of product name:'))

url_categories = 'https://price-api.datayuge.com/api/v1/compare/list/categories'
url_search = "https://price-api.datayuge.com/api/v1/compare/search"
url_detail = "https://price-api.datayuge.com/api/v1/compare/detail"

querystring = {"api_key":api_key,"product":search_input}
headers = {'content-type': 'application/json'}

response_search = requests.request("GET", url_search, headers=headers, params=querystring)
#res_sear_json = response_search.text.read()
res_sear_json_actual = json.loads(response_search.text)

for i in range(len(res_sear_json_actual['data'])):
	print(res_sear_json_actual['data'][i]['product_title'])

exact_name = str(input('Enter exact title of product:'))
