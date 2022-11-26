import requests

#local testing
url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

#web testing. lambda function exposed via api gateway
#url = FOR SECURITY REASONS \
# copy this part from inside aws api gateway and add '/predict'

data = {'url': 'http://bit.ly/mlbookcamp-pants'}

result = requests.post(url, json=data).json()
print(result)