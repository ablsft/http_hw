import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""

        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

        params = {
            "path": file_path 
        }
        headers = {
            "Authorization": self.token
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code not in range(200, 300):
            print('Error while requesting URL')
            return

        url_for_upload = response.json().get('href', '')

        with open(file_path, 'rb') as f:
            response2 = requests.put(url_for_upload, files={"file": f})

        if response2.status_code == 201:
            print('File has been uploaded successfully!')
        else:
            print('Error while uploading file')

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'test.jpg'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)