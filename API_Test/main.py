import requests

# вытаскиваю токен из файла

with open('token_ya.txt') as f:
    token = f.read()

# функция для создания папки, если такая папка уже есть, то она создаёт
# эту папку с индексом "(i)", где i последовательно увеличивается

def folder_maker(token: str, path: str):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Authorization': token}
    params = {'path': path}
    response = requests.put(url, headers=headers, params=params)
    if response.status_code == 409:
        i = 1
        while response.status_code == 409:
            params['path'] = params['path'] + f'({i})'
            response = requests.put(url, headers=headers, params=params)
            i += 1
    elif response.status_code == 401:
        return 'не авторизован'
    return response.status_code


