import requests
import json 
if __name__ == '__main__':
    url = 'http://httpbin.org/delete'
    payload = { 'nombre':'Yoniel','curso':'python','nivel':'intermedio' }
    response = requests.delete(url, data=json.dumps(payload))
    print(response.url)

    if response.status_code == 200:
        headers_response = response.headers #dic
        server = headers_response['server']
        print(server)