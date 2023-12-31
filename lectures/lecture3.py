#ТИПЫ ДАННЫХ: ЧИСЛА, КОРТЕЖИ, СТРОКИ

#Переменные в питоне имеют типов, типы имею только объекты, на которые они ссылаются
#В Питоне типы данных деляться на две принципиальные категории: неизменяемые и изменяемые
#К неизменяемым относятся: числа, строки, кортежи, frozen set
#Для определения типа в Питоне есть функция type()
#Пример использования:
# type('a') -> class <str>
# type('a').name -> 'str'
# Отдельно есть функция, проверяющая, является ли объект представителем конкретного класса
# isinstance(obj, cls) -> bool

#Обсудим числа
#В Питоне есть 3 типа чисел:

#1. Целые числа:
# Целые числа неизменяемы
# В Питоне зарезерированы все числовые значения от -5 до 256(то есть память под них аллоцируетмся в момент запуска программы
# Целочисленные литералы бывают в 2, 8, 10, 16-чных системах счисления
# Можно разделять разряды с помощью нижних подчеркиваний(1_000_000)
#2. Число с плавающей точкой:
# Аналогичны по работе числам с плавающей точки в Си
# Валидные литералы - литералы, в которые входят точки, числа и символ экспоненты:
# 0. ; .0 ; 1.0 ; 1.0e-1
#3. Комплексные числа(comp)
# Имеет структуру a + bj

# Преобразования и операции над числами:
# При операции между разными типами данных Питон приводит все типы на наибольшему(по принципу int < float < complex)
# Кроме того, типы можно привести явно
# Операции над числами практически совпадают с операциями в реальной жизни, так что остановимся на делении
# Есть три типа деления: целочисленное, настоящее и модульное
# Кроме того определены побитовые операции(над целыми числами) (~, &, |, ^, >>, <<)


# ИТЕРИРУЕМЫЕ ОБЪЕКТЫ, ПОСЛЕДОВАТЕЛЬНОСТИ
# Итераируемые объект - объект, поддерживающий функция iter, возвращающе итератор, который поддерживает функция next
# Итераторы могут быть органиченным и неограниченными
# Последовательности тоже являются интерируемыми объектами(упорядоченные), но для них определено еще две операции __len__ и __getitem__(обязательно целочисленная)
# Теперь мы можем понять, как устроен цикл for "под капотом":
#  _iterator = iter(iterable)
# while True:
#   try:
#       x =  next(_iterator)
#    except:
#       break
#   do_something
# К последовательностям в Питоне относятся строки, списки и кортежи
# Общие операции последовательностей:
# 1. Конкатенация
# 2. Оператор повторения
# 3. Оператор in
# 4. Индексация
# 5. Определена операция среза


#КОРТЕЖИ
#Способы объявления
# 1, 2, 5
# 1
# (1, 2, 5)
# ()
# (1,)
# У кортежа есть помимо методов последовательности методы index и count

#СПИСКИ
#Способы объявления:
# [1, 2, 3]
# [1]
# list(1, 2, 3)
# Списки могут быть модифицированны через индексацию и даже срезы
# a[i:i] = k - вот такой ебантизм вставляет в массив k перед i-тым элементом
# Модифицирующие методы:
# .append(), .pop(), .insert(), .reverse(), .sort(key = None, reverse = False) (key - функция, которая сопоставляет элементу некоторое значение), .extend(x) - дописывает объекты x в конец исзодного объекта
        

