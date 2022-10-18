import requests

if __name__ == '__main__':
    client_id = 'dd59550e2f435c9a1f0d'
    client_secret =  '4694115f8f5322ef366ab6ce3af3c21d94cc6f82'
    code = 'b9051f592fc55a8aa8fd'

    access_token = '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'

    url = 'http://api.github.com/user/repos'
    payload = { 'name' : 'api_python' }
    headers = { 'Accept' : 'application/json', 'Authorization' : 'token ' + access_token }

    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print( response.json() )
    else:
        print(response.content)
