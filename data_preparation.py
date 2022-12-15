import pandas as pd
from pandas_profiling import *
import os
import seaborn as sns
from data_reading import *
import matplotlib.pyplot as plt


def remove_zeros(full_df: pd.DataFrame) -> pd.DataFrame :
    # remove zeros from dataframe
    return full_df.loc[:, (full_df != 0).any(axis=0)]


def make_pair_plots(full_df: pd.DataFrame, x_variables: list, y_variables: list, save_plots_fp: str) -> None:
    """
    to make scatter matrix
    :return: None
    """
    sns.set_theme(style="ticks")
    sns.pairplot(full_df, x_vars=x_variables, y_vars=y_variables)
    # fig = scatter_matrix.get_figure()
    os.chdir(save_plots_fp)
    plt.savefig("scatter_matrix_hsp.png", dpi=1000)
    return None


def pandas_profiling_report(full_df: pd.DataFrame, save_report_fp: str) -> None:
    profile = ProfileReport(full_df, title="Pandas Profiling Report")
    os.chdir(save_report_fp)
    profile.to_file("HSP_report.html")
    return None


def data_pre_processing(calculated_data_fp: str, experimental_data_fp: str, save_report_fp: str,
                        save_plots_fp: str, plot_variables: dict) -> pd.DataFrame:
    #     get dataframe
    full_df = pd.DataFrame(dataset_df(calculated_data_fp, experimental_data_fp))
    #     remove zeros
    remove_zeros_df = remove_zeros(full_df)
    #     create pandas profiling report
    pandas_profiling_report(full_df, save_report_fp)
    #     create scatter matrix
    make_pair_plots(full_df, plot_variables["x_variables"], plot_variables["y_variables"], save_plots_fp)
    #     return dataframe
    return remove_zeros_df
