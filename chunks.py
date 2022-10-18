import requests

if __name__ == '__main__':
    url = 'https://i.blogs.es/ceda9c/dalle/450_1000.jpg'

    response = requests.get(url, stream=True) #Realizar la peticion sin descargar el contenido 
    with open('image.jpg', 'wb') as file:
        for chunk in response.iter_content(): #Descargar el contenido poco a poco 
            file.write(chunk)

    response.close()