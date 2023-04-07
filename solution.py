import pandas as pd
import numpy as np


chat_id = 1283808304

def solution(x: np.array) -> float:
    n = len(x)
    time = 10
    errors = np.random.exponential(scale=1, size=n) - 15
    v_real = x - errors
    a = pow(sum(np.square(v_real))/n, 0.5) /(time)
    return a
