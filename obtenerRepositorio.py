import requests
client_id = 'dd59550e2f435c9a1f0d'
client_secret =  '4694115f8f5322ef366ab6ce3af3c21d94cc6f82'

code = 'b9051f592fc55a8aa8fd'
access_token = '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'

if __name__ == '__main__':
    url = 'http://api.github.com/user/repos'
    headers = { 'Authorization' : 'token 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' }

    response = requests.get(url, headers=headers)
    if response.status_code == 200: 
        payload = response.json()

        for project in payload:
            name = project['name']
            print(name)
    else:
        print(response.content)