from sklearn.metrics import mean_squared_error, \
    mean_absolute_error, r2_score
import numpy as np
import pandas as pd


def metrics(y_pred: list, y_true: list) -> dict:
    # calculate mae
    mae = mean_absolute_error(y_true, y_pred)
    print(f"MAE = {mae}")
    # calculate rmse
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    print(f"RMSE = {rmse}")

    # calculate R^2
    r_squared = r2_score(y_true, y_pred)
    print(f"R$^{2}$ = {r_squared}")

    return {"R_2": r_squared, "mae": mae, "rmse":rmse }