import pandas as pd
import numpy as np


chat_id = 1283808304

def solution(x: np.array) -> float:
    n = len(x)
    time = 10
    errors = np.random.exponential(1, n) - 15
    v_real = x + errors
    a = (1/(n*time)) * np.sum(v_real)
    return a
