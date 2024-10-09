# Проект 0. Угадай число

## Оглавление
[1. Описание проекта](https://github.com/Beinterpreter/sf_data_science/tree/main/project_0#%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)  
[2. Какой кейс решаем?](https://github.com/Beinterpreter/sf_data_science/tree/main/project_0#%D0%BA%D0%B0%D0%BA%D0%BE%D0%B9-%D0%BA%D0%B5%D0%B9%D1%81-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC)  
[3. Краткая информация о данных](https://github.com/Beinterpreter/sf_data_science/tree/main/project_0#%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)  
[4. Этапы работы над проектом](https://github.com/Beinterpreter/sf_data_science/tree/main/project_0#%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)  
[5. Результат](https://github.com/Beinterpreter/sf_data_science/tree/main/project_0#%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82)  
[6. Выводы](https://github.com/Beinterpreter/sf_data_science/tree/main/project_0#%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B)  

### Описание проекта
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up: [К оглавлению](https://github.com/Beinterpreter/sf_data_science/tree/main/project_0#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### Какой кейс решаем?
Нужно написать программу, которая угадывает число за минимальное число попыток.

**Условия соревнования:**
- Компьютер загадывает число от 0 до 100, а нам нужно его угадать. Под "угадать" подразумевается "написать программу, которая угадывает число".
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**  
Результаты оцениваются по среднему количеству попыток при 1000 повторений.

**Что практикуем**  
Учимся писать хороший код на Python

### Краткая информация о данных
....

:arrow_up: [К оглавлению](https://github.com/Beinterpreter/sf_data_science/tree/main/project_0#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### Этапы работы над проектом
....

:arrow_up: [К оглавлению](https://github.com/Beinterpreter/sf_data_science/tree/main/project_0#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

##  Результат  
Созданная программа угадывает число в среднем за 5 попыток при 1000 повторений.

:arrow_up: [К оглавлению](https://github.com/Beinterpreter/sf_data_science/tree/main/project_0#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### Выводы
В созданной программе применен алгоритм динамического сужения границ диапазона поиска загаданного числа с использованием медианного значения текущего диапазона поиска в качестве нового предополагаемого числа. Данный алгоритм угадывает число в среднем за 5 попыток, что в 4 раза эффективнее максимального допустимого порога в 20 попыток.

:arrow_up: [К оглавлению](https://github.com/Beinterpreter/sf_data_science/tree/main/project_0#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами

