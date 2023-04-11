import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 157443210 # Ваш chat ID, не меняйте название переменной

def solution(...) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return ... # Ваш ответ, True или False

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    _, p_value = ttest_ind(x, y, equal_var=False)
    alpha = 0.07
    return p_value < alpha
