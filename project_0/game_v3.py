import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Угадываем число за минимум попыток путем сужения границ диапазона поиска
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0 # Счетчик числа попыток
    predict_nr = np.random.randint(1, 101) # Предоплагаемое число
    # Минимальное значение диапазона поиска
    min_limit = 1 
    # Максимальное значение диапазона поиска
    max_limit = 101 

    while predict_nr != number:
      count += 1
      # Сужаем границы диапазона поиска перемеащая минимум или максимум
      if predict_nr < number:
        min_limit = predict_nr               
      else: # Если предполагаемое число больше загаданного
        max_limit = predict_nr
      
      # Если в диапазоне между минимумом и максимумом одно число, делаем его предполагаемым
      if len(range(min_limit, max_limit)) == 2:
        predict_nr = (range(min_limit, max_limit))[1]
      else: # в противном случае, делаем предполагаемым числом медиану текущего диапазона
        predict_nr = int(np.mean(range(min_limit, max_limit)))           
  
    return count