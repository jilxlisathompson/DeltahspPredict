import unittest
from data_reading import *
import openpyxl


class MyTestCase(unittest.TestCase):
    def test_ReadOutputData(self):
        """
        also for TestReadExperimentalData
        :return:
        """
        filepath_output = "/Users/eh19686/Documents/PhD/conducting_polymer_project/moe_output_data/new_monomers_lowest_data.txt"
        self.assertTrue(type(filepath_output), "<class 'str'>")
        # test that output is a pandas dataframe
        output_df = read_output_data(filepath_output)
        self.assertTrue(type(output_df), "<class 'pandas.core.frame.DataFrame'>")
        # test that it reads *.csv, *.txt and *.xlsx files

    # def test_ReadCSVExtra(self):
    #     # test if the columns are deleted
    #     column_names = ['deltaD', 'DeltaP', 'DeltaH']
    #     filepath_exp = "/Users/eh19686/Documents/PhD/conducting_polymer_project/moe_output_data/new_monomers_lowest_data.txt"
    #     exp_data_output = read_csv_extra(filepath_exp)
    #     print("here in the test function")
    #     print(exp_data_output)
    #     exp_data_output_colnames = exp_data_output.keys().tolist()
    #     self.assertTrue(column_names.intersection(exp_data_output_colnames), column_names)

    def test_Dataset_DF(self):
        # check return dataframe
        filepath_exp = "/Users/eh19686/Documents/PhD/conducting_polymer_project/HSP_project_p1/dataset/adts201800069-sup-0002-polymers_exp.csv"
        filepath_output = "/Users/eh19686/Documents/PhD/conducting_polymer_project/moe_output_data/new_monomers_lowest_data.txt"
        data_df = dataset_df(filepath_exp, filepath_output)
        self.assertTrue(type(data_df), "<class 'pandas.core.frame.DataFrame'>")
        self.assertTrue(type(data_df), "<class 'pandas.core.frame.DataFrame'>")


if __name__ == '__main__':
    unittest.main()
