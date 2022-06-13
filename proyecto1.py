import json
import requests 
def leerArchivo():
    lista:list = []
    with open('input.txt','r') as texto:
        for i in texto:
            lista.append(i.split())
        return lista
def get(registro):
    resultadoLista:list = []
    for x in registro:
        for i in x:
            url = f'https://api.mercadolibre.com/sites/MLA/search?seller_id={i}'
            requestGet = requests.get(url)
            get_obtenido = requestGet.json()
            try:
                item = get_obtenido['results'][0]['id']
                title = get_obtenido['results'][0]['title']
                category = get_obtenido['results'][0]['category_id']
                name = get_obtenido['results'][0]['domain_id']
                resultadoLista.append(f'{item} con titulo {title} pertenece  la categoria {category} nombre: {name}')
            except IndexError as e:
                print(f'El seller {i} no tiene item')
            with open('output.txt','w') as output:
                for i in resultadoLista:
                    output.write(i + '\n')



if __name__ == '__main__':
    registro = leerArchivo()
    get(registro)