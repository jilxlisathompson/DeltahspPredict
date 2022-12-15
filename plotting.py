import pandas as pd
import os
from model_building import *
import matplotlib.pyplot as plt
import seaborn as sns

def plot_cv_results(df: pd.DataFrame, hansen_parameter: str,
                    save_plot_fp: str) -> None:
    # get cv_results
    cv_results, cv_params = kfold_cv_as_loocv(df, hansen_parameter)
    # plotting cv results
    plt.figure(figsize=(6, 6))

    plt.plot(cv_results["param_n_features_to_select"],
             cv_results["mean_test_score"])
    plt.plot(cv_results["param_n_features_to_select"],
             cv_results["mean_train_score"])
    plt.xlabel("number of features")
    plt.ylabel("rmse")
    plt.title("Optimal number of features")
    plt.legend(["test score", "train score"], loc="lower right")
    plt.show()

    # enter directory which save plot is stored
    os.chdir(save_plot_fp)
    # saving plot
    user_input = input("Would you like to save plot, answer y or n:")

    if user_input == "y":
        plt.savefig("k_fold_cross_validation_results.png", dpi=1000)
    elif user_input == "n":
        print("okay, plot will not be saved.")


    return None