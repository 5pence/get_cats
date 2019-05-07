import requests, os, shutil


def save_image(full_path, name, data):
    file_name = os.path.join(full_path, name + '.jpg')
    with open(file_name,'wb') as fout:
        shutil.copyfileobj(data, fout)


def get_cat(full_path, name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_data_from_url(url)
    save_image(full_path, name, data)


def get_data_from_url(url):
    response = requests.get(url, stream=True)
    return response.raw
