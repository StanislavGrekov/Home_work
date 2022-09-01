from time import time
import requests
import json
import sys
import datetime, time
from pprint import pprint
import os

############1 задание###############

url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
response = requests.get(url)
answer = json.loads(response.text) # Десерилизация в переменную по строкам
list_of_heroes = ['Hulk', 'Captain America', 'Thanos']
my_dict = {}
for element_list in list_of_heroes:
    for element_answer in answer:
        for element_key, element_values in element_answer.items():
            if element_list == element_values:
                my_dict[element_list] = element_answer['powerstats']['intelligence']
max_val = max(my_dict.values())  #находим максимальное значение в словаре
final_dict = {k:v for k, v in my_dict.items() if v == max_val} #Создаем словарь, где будет ключ с максимальным значением 
print(final_dict)

##### А это правильное решение без цикла в цикле)))))##########
# list_of_heroes = ['Hulk', 'Captain America', 'Thanos']
# my_dict = {}
# for element in answer:
#     if element['name'] in list_of_heroes:
#         my_dict[element['name']] = element['powerstats']['intelligence']


#################Задание №2###############

class YaDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self,  disk_file_path):
        file_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, "overwrite": "true"}
        response = requests.get(file_url, params = params, headers = headers)
        #pprint(response.json())
        return response.json()

    def upload_file_to_disk(self,  disk_file_path, file):
        response_link = self._get_upload_link(disk_file_path =  disk_file_path)
        href = response_link.get('href', '')
        response = requests.put(href, data = open(file, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('File uploaded!')

    def category_created(self, path_to_file): # Данный метод создает папку на яндекс диске
        file_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': path_to_file, "overwrite": "true"}
        response = requests.put(file_url, headers = headers, params = params)
        response.raise_for_status()
        if response.status_code == 201:
            print('Сategory created!')

    def processing(self, path_to_disk): # Данный метод обрабатывает имена файлов (приводит их к str), затем содает два параметра которые подставляем в метод upload_file_to_disk
        list_of_files = os.listdir(path_to_disk)
        for element in list_of_files:
            name_of_file = ''.join(element)
            param_1 = category_on_YaDisk +'/'+ name_of_file
            param_2 = path_to_disk+'/'+name_of_file
            ya.upload_file_to_disk(param_1,param_2)

if __name__ == '__main__':
    ya = YaDisk('                                                              ')
    category_on_YaDisk = 'upload'
    path_to_disk = 'D:/Python/Home_work_Requests/test'
    ya.category_created(category_on_YaDisk)
    ya.processing(path_to_disk)

''' Работает, только если на Яндекс диске не создана папка. Если создана ничего не перезаисывается и программа падает с ошибкой 409, хотя указаны параметры "overwrite": "true".
Так и не разобрался почему так происходит.'''


##############Задание №3###############

def questions_with_python():
    # Получаем в секундах текущую дату минус 2 дня
    today = datetime.date.today()
    day = today.day - 2
    t = datetime.datetime(today.year, today.month, day)
    second = round(t.timestamp())
    #Задаем параметры и URL сайта stackexchange.com. Указываем в качестве тега Python
    params = {'todate': second, 'order':'desc', 'sort':'activity','tagged':'python','site':'stackoverflow' }
    url = "https://api.stackexchange.com/2.3/questions"
    # Выполняем get запрос, ответ от сайта преобразуем в json, в котором с помощью цикла находим значения по ключу title.
    response = requests.get(url,params=params)
    answer = json.loads(response.text)

    for item in answer['items']:
        for key, values in item.items():
            if key == 'title':
                print(values)

questions_with_python()
