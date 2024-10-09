import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0 # Счетчик числа попыток
    predict_nr = np.random.randint(1, 101) # Предоплагаемое число
    min_limit = 1
    max_limit = 101

    while predict_nr != number:
      count += 1
      
      if predict_nr < number:
        min_limit = predict_nr               
      else:
        max_limit = predict_nr

      if len(range(min_limit, max_limit)) == 2:
        predict_nr = (range(min_limit, max_limit))[1]
      else:
        predict_nr = int(np.mean(range(min_limit, max_limit)))  
         
    # Ваш код заканчивается здесь

    return count

print(game_core_v3(4))

