import json
import bs4
import requests
import urllib.request

def bulletins(debug=False, base_url = 'https://covid19cubadata.github.io/'):
    _bulletins = []

    source = requests.get(f'{base_url}boletines').text

    soup = bs4.BeautifulSoup(source,'lxml')

    for elem in soup.findAll('a'):
        description = elem.text
        link = elem.get('href')
        number = description[description.find('No.') + 4]
        size = int(urllib.request.urlopen(base_url + link).info()['Content-Length'])/10**6
        _bulletins.append({
            'id': number,
            'info': description,
            'url': link,
            'size': size})

    _bulletins.sort(key= lambda x : x['id'])

    data = [
        {
            'name': 'CEDEM',
            'url': 'http://www.biblioteca.uh.cu/red-bibliotecas/centro-estudios-demograficos-cedem',
            'data_source': base_url,
            'bulletins': _bulletins
        }
    ]

    return data
    