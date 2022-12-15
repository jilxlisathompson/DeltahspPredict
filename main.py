from data_preparation import *


def main():
    output_fp = "/Users/eh19686/Documents/PhD/conducting_polymer_project/moe_output_data/new_monomers_lowest_data.txt"
    experimental_fp = "/Users/eh19686/Documents/PhD/conducting_polymer_project/HSP_project_p1/dataset/adts201800069-sup-0002-polymers_exp.csv"
    report_fp = "/Users/eh19686/Documents/PhD/conducting_polymer_project/moe_output_data"
    print(read_output_data(output_fp))

    final_df = dataset_df(output_fp, experimental_fp)
    final_df.keys()

    return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
