import pandas as pd


def read_output_data(filepath_output: str) -> dict:
    # check file type
    # options --> *.xlsx, *.txt, *.csv
    # check end of file
    # if file.endswith an of the above options
    # use appropriate pandas function i.e. pd.read_csv(), pd.read_excel()
    data_fp = filepath_output
    data_fp = data_fp.split("/")[-1]
    if data_fp.endswith(".csv") or data_fp.endswith(".txt"):
        data_df = pd.read_csv(filepath_output, sep=",")
    elif data_fp.endswith(".xlsx"):
        data_df = pd.read_excel(filepath_output)

        # return pd.dataframe of data
    return data_df


def read_experimental_data(filepath_exp) -> dict:
    # check file type
    # options --> *.xlsx, *.txt, *.csv
    # check end of file
    # if file.endswith an of the above options
    # use appropriate pandas function i.e. pd.read_csv(), pd.read_excel()
    # exp_data_df = pd.DataFrame()
    experimental_fp = filepath_exp.split(",")[-1]
    if experimental_fp.endswith(".csv"):
        return pd.read_csv(filepath_exp, sep=",")
        # exp_data_df = pd.read_csv(filepath_exp, sep=",")
    elif experimental_fp.endswith(".xlsx"):
        return pd.read_excel(filepath_exp)
        # exp_data_df = pd.read_excel(filepath_exp)

    # print(exp_data_df)

    # return pd.dataframe of data
    # return exp_data_df


def read_csv_extra(filepath_exp: str) -> dict:
    """
    :param filepath_exp:
    :return:
    """
    exp_data_df = pd.DataFrame(read_experimental_data(filepath_exp))
    print("Here in read csv extra")
    print(exp_data_df.keys())
    exp_data_df2 = exp_data_df[["label", 'DeltaD', 'DeltaP', 'DeltaH', 'smiles', 'n_electrons', 'n_atoms', 'charge', 'MolWt']]

    return exp_data_df2


def dataset_df(fp_exp, fp_output) -> dict:
    # put together final dataframe
    # if the first column is 'label' then call read_csv_extra
    exp_data_df = read_experimental_data(fp_exp)
    if exp_data_df["label"].any():
        exp_data_df = read_csv_extra(fp_exp)

    output_data_df = read_output_data(fp_output)
    # to create full_dataframe compare columns="mol"
    # concatenate dataframes along columns
    full_dataframe = pd.concat([exp_data_df, output_data_df], axis=1)

    return full_dataframe
