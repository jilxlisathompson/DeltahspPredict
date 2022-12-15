import unittest
from data_preparation import *
from data_reading import *


class MyTestCase(unittest.TestCase):

    def test_RemoveZeros(self):
        # reading in data
        fp_exp = "/Users/eh19686/Documents/PhD/conducting_polymer_project/HSP_project_p1/dataset/adts201800069-sup-0002-polymers_exp.csv"
        fp_calc = "/Users/eh19686/Documents/PhD/conducting_polymer_project/moe_output_data/new_monomers_lowest_data.txt"
        full_df = dataset_df(fp_exp, fp_calc)
        # call remove zeros
        df = remove_zeros(full_df)
        # check if there are any zeros in dataframe
        self.assertEqual(0 in df.values, True)

    def test_MakePairPlots(self):
        # read in data
        # make pair plots
        # check in directory if pair plots have been saved
        pass
    def test_PandasProfilingReport(self):
        pass
    def test_DataPreProcessing(self):
        pass


if __name__ == '__main__':
    unittest.main()
