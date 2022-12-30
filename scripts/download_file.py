import requests

def download(url):
    get_response = requests.get(url)
    file_name = get_response.content.split("/")[-1]
    with open(file_name, "w") as out_file:
        out_file.write(get_response.content)