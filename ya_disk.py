import requests


class YaUploader:
    def __init__(self, token, file_path: str):
        self.file_path = file_path
        self.token = token
        print(file_path[41:])

    def upload(self, disk_file_path):
        """Метод загруджает файлы по списку file_list на яндекс диск"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        file_json = response.json()
        href = file_json.get("href", "")
        response_load = requests.put(href, data=open(self.file_path, 'rb'))
        response_load.raise_for_status()
        if response.status_code == 201:
            print("Success")
