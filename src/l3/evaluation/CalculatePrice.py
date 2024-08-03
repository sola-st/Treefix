import argparse
import pandas as pd

from ..Util import gather_files


parser = argparse.ArgumentParser()
parser.add_argument(
    "--files", help="CSV files containing the predictions from the model", nargs="+")

if __name__ == "__main__":
    args = parser.parse_args()

    files = gather_files(args.files)

    total_s1_input_size = 0
    total_s1_output_size = 0

    total_s2_input_size = 0
    total_s2_output_size = 0

    total_s3_input_size = 0
    total_s3_output_size = 0

    for file in files:
        df = pd.read_csv(file)
        for index, row in df.iterrows():
            print(f"row {index}")

            if row['prompt_type'] == 1:
                total_s1_input_size += row['input_size']
                total_s1_output_size += row['output_size']
            elif row['prompt_type'] == 2:
                total_s2_input_size += row['input_size']
                total_s2_output_size += row['output_size']
            elif row['prompt_type'] == 3:
                total_s3_input_size += row['input_size']
                total_s3_output_size += row['output_size']            

    # GPT-4o-mini
    s1_input_price = float(0.15 * total_s1_input_size) / 1000000
    s1_output_price = float(0.60 * total_s1_output_size) / 1000000
    
    s2_input_price = float(0.15 * total_s2_input_size) / 1000000
    s2_output_price = float(0.60 * total_s2_output_size) / 1000000
    
    s3_input_price = float(0.15 * total_s3_input_size) / 1000000
    s3_output_price = float(0.60 * total_s3_output_size) / 1000000

    # GPT-4o
    # s1_input_price = float(5 * total_s1_input_size) / 1000000
    # s1_output_price = float(15 * total_s1_output_size) / 1000000
    
    # s2_input_price = float(5 * total_s2_input_size) / 1000000
    # s2_output_price = float(15 * total_s2_output_size) / 1000000
    
    # s3_input_price = float(5 * total_s3_input_size) / 1000000
    # s3_output_price = float(15 * total_s3_output_size) / 1000000
   
    avg_s1_input_price = s1_input_price / len(files)
    avg_s1_output_price = s1_output_price / len(files)

    avg_s2_input_price = s2_input_price / len(files)
    avg_s2_output_price = s2_output_price / len(files)

    avg_s3_input_price = s3_input_price / len(files)
    avg_s3_output_price = s3_output_price / len(files)

    
    print(f"Avg S1 Input price: ${avg_s1_input_price}")
    print(f"Avg S2 Input price: ${avg_s2_input_price}")
    print(f"Avg S3 Input price: ${avg_s3_input_price}")

    print(f"Avg S1 Output price: ${avg_s1_output_price}")
    print(f"Avg S2 Output price: ${avg_s2_output_price}")
    print(f"Avg S3 Output price: ${avg_s3_output_price}")

    total_price = s1_input_price + s2_input_price + s3_input_price
    total_price += s1_output_price + s2_output_price + s3_output_price
    print(f"Total price: ${total_price}")

    avg_total_price = avg_s1_input_price + avg_s2_input_price + avg_s3_input_price
    avg_total_price += avg_s1_output_price + avg_s2_output_price + avg_s3_output_price
    print(f"Avg price: ${avg_total_price}")

