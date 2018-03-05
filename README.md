# Ближайшие бары

**bars.py** расчитывает:
 - самый большой бар по количеству мест
 - самый маленький бар по количеству мест
 - самый близкий бар (текущие gps координаты пользователь вводит с клавиатуры )

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5 и библиотеки **geopy**

```bash

pip install geopy

```

Запуск на Linux:

```bash

$ python bars.py # possibly requires call of python3 executive instead of just python
Enter your longtude: 37.6
Enter your latutude: 55.7
The biggest bar: Спорт бар «Красная машина» with 450 seats
The smallest bar: БАР. СОКИ with 0 seats
The closest bar: БИР-ТАЙМ distance: 1893.25 meters

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
