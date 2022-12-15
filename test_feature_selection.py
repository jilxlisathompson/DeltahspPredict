import unittest
from feature_selection import recursive_feature_elimination_cv
from data_reading import *
import pandas as pd
import os


class MyTestCase(unittest.TestCase):

    def test_RFECV(self):
        # experimental data fp

        filepath_exp = "/Users/eh19686/Documents/PhD/conducting_polymer_project/HSP_project_p1/dataset/adts201800069-sup-0002-polymers_exp.csv"
        filepath_output = "/Users/eh19686/Documents/PhD/conducting_polymer_project/moe_output_data/new_monomers_lowest_data.txt"
        data_df = dataset_df(filepath_exp, filepath_output)
        print(data_df.keys())
        # print(data_df["smiles"])
        # insert new column into dataframe
        # list of column names
        # os.chdir("/Users/eh19686/Documents/PhD/conducting_polymer_project/moe_output_data/dataset2")
        # data_df.to_excel("data_HSP_paper.xlsx")
        column_names = ["p_1001", "p_1004", "p_1007", "p_1010", 'p_1013', 'p_1016', 'p_1019', 'p_1022',
                        'p_1025', 'p_1028', 'p_1031', 'p_1002', 'p_1005', 'p_1008', 'p_1011', 'p_1014', 'p_1017',
                        'p_1020', 'p_1023', 'p_1026', 'p_1029', 'p_1003', 'p_1006', 'p_1009', 'p_1012', 'p_1015',
                        'p_1018', 'p_1021', 'p_1024', 'p_1027', 'p_1030']

        idx = 0
        data_df.insert(loc=idx, column='filenames', value=column_names)
        data_df.drop(['label', 'smiles', 'n_electrons', 'n_atoms', 'charge', 'MolWt'], axis=1, inplace=True)
        os.chdir("/Users/eh19686/Documents/PhD/conducting_polymer_project/moe_output_data/dataset2")
        data_df.to_excel("data_HSP_paper.xlsx")
        # reading in other data
        additional_data_fp = "/Users/eh19686/Documents/PhD/conducting_polymer_project/moe_output_data/moe_output_data.xlsx"
        additional_data_df = pd.read_excel(additional_data_fp)
        # rename columns
        additional_data_df.rename(columns={'file name ': "filenames","D": "DeltaD", "P": "DeltaP", "H": "DeltaH"}, inplace=True)
        additional_data_df.drop(['Unnamed: 0', 'mol', 'structures '], axis=1, inplace=True)
        print("here is additional df")
        print(additional_data_df)
        print(additional_data_df.keys())
        additional_data_df.to_excel("og_data.xlsx")
        # rename
        # concatenating dfs
        frames = [data_df, additional_data_df]
        full_df = pd.concat(frames, axis=1)
        print(full_df["filenames"].values.tolist())

        # read in data
        #
        self.assertTrue(type(filepath_exp), "str")


if __name__ == '__main__':
    unittest.main()
