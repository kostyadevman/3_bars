# Ближайшие бары

**bars.py** расчитывает:
 - самый большой бар по количеству мест
 - самый маленький бар по количеству мест
 - самый близкий бар (текущие gps координаты пользователь вводит с клавиатуры )

# Как запустить
На сайте data.mos.ru есть много разных данных, в том числе список московских баров. Его можно скачать в формате JSON. Для этого нужно:

- зарегистрироваться на сайте и получить ключ API;
- скачать файл по ссылке вида https://apidata.mos.ru/v1/features/1796?api_key={place_your_API_key_here}.
 
 А можно не тратить на это время и воспользоваться файлом bars.json или [скачать](https://devman.org/fshare/1503831681/4/).

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5 и библиотеки **geopy**

```bash

$ pip install -r requirements.txt

```

Запуск на Linux:

```bash

$ python bars.py <path to file> # possibly requires call of python3 executive instead of just python
Enter your longtude: 37.6
Enter your latutude: 55.7
The biggest bar:
Name: Спорт бар «Красная машина»
Seats count: 450
Distance to bar: 4244.09 meters
  
The smallest bar: 
Name: БАР. СОКИ
Seats count: 0
Distance to bar: 29801.59 meters
 
The closest bar: 
Name: БИР-ТАЙМ
Seats count: 28
Distance to bar: 1893.25 meters

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
