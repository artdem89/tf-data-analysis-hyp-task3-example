import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
from statsmodels.stats.weightstats import ztest

chat_id = 157443210 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    z_statistic, p_value = ztest(x, y)
    alpha = 0.01
    return p_value < alpha
