import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'

token = 'sdsdsdadadasd2222333'
username = 'vladimirjanexxx'
pixel_id = 'graph1'

user_params = {
    'token': token,
    'username': username,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}


graph_endpoint = f'{pixela_endpoint}/{username}/graphs'

graph_config = {
    'id': pixel_id,
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN': token
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_post = f'{pixela_endpoint}/{username}/graphs/{pixel_id}'

today = datetime(year=2022,month=12,day=26)

pixel_config = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '16'

}

# response_pixel = requests.post(url=pixel_post, json=pixel_config, headers=headers)
# print(response_pixel.json())
#
# update_endpoint = f'{pixela_endpoint}/{username}/graphs/{pixel_id}/{today}'
#
# new_pixel_data = {
#     'quantity': '4.5'
# }
#
# requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.json())

# delete_pixel = f"{pixela_endpoint}/{username}/graphs/{pixel_id}/{today.strftime('%Y%m%d')}"
#
# delete_req = requests.delete(url=delete_pixel, headers=headers)
# print(delete_req.json())
