import requests
client_id = 'dd59550e2f435c9a1f0d'
client_secret =  '4694115f8f5322ef366ab6ce3af3c21d94cc6f82'

code = 'b9051f592fc55a8aa8fd'
access_token = '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'
if __name__ == '__main__':
    url = 'https://github.com/login/oauth/access_token'
    payload = { 'client_id' : client_id, 'client_secret' : client_secret, 'code' : code }
    headers = {'Accept' : 'application/json'}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_json = response.json()

        access_token = response_json['access_token']
        print(access_token)