from pprint import pprint
import os

print('#####################################################1 задание#########################################')
with open("recipes.txt", encoding="utf-8") as f:
    cook_book = {}
    for str in f:
      ingridients = []
      
      name_dish = str.strip()
      number_ingridient = int(f.readline().strip())
      for i in range(number_ingridient):
       ingridient_dict = {}
       item1,item2,item3 = f.readline().strip().split("|")
       ingridient_dict['ingredient_name'] = item1
       ingridient_dict['quantity'] = item2
       ingridient_dict['measure'] = item3
             
       ingridients.append(ingridient_dict)
      cook_book[name_dish] = ingridients
      null_string = f.readline()  

  
pprint(cook_book)
print()

print('##################################################2 задание#########################################')
cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ]
  }

def my_func(dish, person_count):
###Обрабатываем первое блюдо из списка dish
  my_dict_dish_1 = {}
  list_ingridient = []
  list_measure = []
  list_quantity = []
  dict_1 ={}
  for key, values in cook_book.items():
      if key == dish[0]:
        for i in values:
          for key, values in i.items():
            if key == 'ingredient_name':
              list_ingridient.append(values)
            elif key == 'measure':
              list_measure.append(values)
            elif key == 'quantity':
              list_quantity.append(values)
  for i in range(len(list_ingridient)):
    list_1 = ['measure','quantity']
    list_2 = [list_measure[i], list_quantity[i]]
    dict_1 = dict(zip(list_1, list_2))
    my_dict_dish_1[list_ingridient[i]] = dict_1
  print('Получили словарь в необходимой форме после обработки ингридеинтов первого блюда:')
  pprint(my_dict_dish_1)
  print()

###Обрабатываем второе блюдо из списка dish
  my_dict_dish_2 = {}
  list_ingridient = []
  list_measure = []
  list_quantity = []
  dict_1 ={}
  for key, values in cook_book.items():
      if key == dish[1]:
        for element in values:
          for key, values in element.items():
            if key == 'ingredient_name':
              list_ingridient.append(values)
            elif key == 'measure':
              list_measure.append(values)
            elif key == 'quantity':
              list_quantity.append(values)
  for i in range(len(list_ingridient)):
    list_1 = ['measure','quantity']
    list_2 = [list_measure[i], list_quantity[i]]
    dict_1 = dict(zip(list_1, list_2))
    my_dict_dish_2[list_ingridient[i]] = dict_1
  print('Получили словарь в необходимой форме после обработки ингридеинтов второго блюда:')  
  pprint(my_dict_dish_2)
  print()
   
###Совмещаем два словаря my_dict_dish_1 и my_dict_dish_2
  
  dict_person = {}
  list_ingridient_person = []
  list_measure_person=[]
  list_quantity_person = []
# Отрабатываем условие, если названия блюд одинаковые:
  if dish[0] == dish[1]:
    for key_dict_dish_1, values_dict_dish_1 in my_dict_dish_1.items():
        list_ingridient_person.append(key_dict_dish_1)
        for key1, values1 in values_dict_dish_1.items():
          if type(values1) == int:
            list_quantity_person.append(values1*person_count*2)
          else:
            list_measure_person.append(values1)  
        for i in range(len(list_ingridient_person)):
            dict_person[list_ingridient_person[i]] = {'measure': list_measure_person[i],'quantity':list_quantity_person[i]}
# Обрабатываем условие, если названия блюд разные:
  else:
    for key_dict_dish_1,values_dict_dish_1 in my_dict_dish_1.items():
      for key_dict_dish_2, values_dict_dish_2 in my_dict_dish_2.items():
        if key_dict_dish_1 == key_dict_dish_2:   # Если названия ингридиентов одинаковые
          list_ingridient_person.append(key_dict_dish_1)
          for key1, values1 in values_dict_dish_1.items():
            if type(values1) == int:
              list_quantity_person.append(values1*2*person_count)
            else:
               list_measure_person.append(values1)  
          for i in range(len(list_ingridient_person)):
            dict_person[list_ingridient_person[i]] = {'measure': list_measure_person[i],'quantity':list_quantity_person[i]}
        else: # Если названия ингридиентов разные то обрабатываем элементы второго словаря
          for key_dict_dish_2, values_dict_dish_2 in my_dict_dish_2.items():
            list_ingridient_person.append(key_dict_dish_2)
            for key1, values1 in values_dict_dish_2.items():
              if type(values1) == int:
                list_quantity_person.append(values1*person_count)
              else:
                 list_measure_person.append(values1)  
            for i in range(len(list_ingridient_person)):
              dict_person[list_ingridient_person[i]] = {'measure': list_measure_person[i],'quantity':list_quantity_person[i]}              
          for key_dict_dish_1, values_dict_dish_1 in my_dict_dish_1.items(): # Если названия ингридиентов разные обрабатываем элементы первого  словаря
            list_ingridient_person.append(key_dict_dish_1)
            for key1, values1 in values_dict_dish_1.items():
              if type(values1) == int:
                list_quantity_person.append(values1*person_count)
              else:
                 list_measure_person.append(values1)  
            for i in range(len(list_ingridient_person)):
              dict_person[list_ingridient_person[i]] = {'measure': list_measure_person[i],'quantity':list_quantity_person[i]}   
            
        
  print('Получили результирующую форму:')
  pprint(dict_person) 
   
my_func([ 'Запеченный картофель', 'Омлет'], 2)
print()

print('#############################################3 задание#########################################')

# Находим нужные файлы в каталоге
BASE_dir = os.getcwd()
way = sorted(os.listdir(BASE_dir))
list_of_files = way[0:3]

# Задаем пустые списки и словарь для обработки
new_dict = {}
number_of_symbols = []
list_content = []
list_sort = []

# Блок кода считавает содержимое из файлов, вычисляет кол-во символов в файле и выдает словарь в виде NUMBER:{FILE:CONTENT}
for file in list_of_files:
    with open(file, encoding="utf-8") as f:
        content = f.read();
        list_content.append(content)
        number = len(content);
        number_of_symbols.append(number)
        new_dict[number] = {file: content}

list_sort = sorted(new_dict.items())   # Выполняем сортировку словаря

# Блок работает со списком list_sort, выполняет запись в файл в виде НАЗВАНИЕ ФАЙЛА, КОЛИЧЕСТВО СИМВОЛОВ, СОДЕРЖАНИЕ ФАЙЛА
with open("write.txt", "w", encoding='utf-8') as file:
    for element in list_sort:
        for key in element[1].keys():
            file.write(str(key)+'\n')
        file.write(str(element[0])+'\n')
        for values in element[1].values():
            file.write(str(values)+'\n')
        file.write('\n')
