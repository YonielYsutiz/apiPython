import requests
import json 
if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    payload = { 'nombre':'Yoniel','curso':'python','nivel':'intermedio' }
    headers = {'Content-Type' : 'application/json', 'access-token' : '12345' }
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    print(response.url)

    if response.status_code == 200:
        #print(response.content)
        headers_response = response.headers #dic
        server = headers_response['Server']
        print(server)