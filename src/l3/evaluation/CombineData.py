import os
import pandas as pd

folder_path = "./metrics/"

# Get a list of used datasets
datasets = os.listdir(folder_path)

for dataset in datasets:
    # Get a list of used predictors
    predictors = os.listdir(folder_path + dataset)

    combined_df_for_dataset = pd.DataFrame()
    
    for predictor in predictors:
        # Get a list of raw metric files
        files = os.listdir(f'{folder_path}{dataset}/{predictor}/raw') 
        # Filter the files to include only the ones that match the pattern "metrics_x.csv"
        files = [file for file in files if file.startswith("metrics__body")]

        combined_df_for_predictor = pd.DataFrame()

        for file in files:
            try:
                df = pd.read_csv(f'{folder_path}{dataset}/{predictor}/raw/{file}')
                combined_df_for_predictor = pd.concat([combined_df_for_predictor, df], ignore_index=True)
            except pd.errors.EmptyDataError:
                print(file)

        files = combined_df_for_predictor["file"].unique()    
        for file in files:
            indexes = combined_df_for_predictor.index[combined_df_for_predictor['file'] == file].tolist()
            for index in indexes[:-1]:
                combined_df_for_predictor = combined_df_for_predictor.drop(index=index)

        combined_df_for_predictor.to_csv(f'{folder_path}{dataset}/{predictor}/metrics_random_functions.csv', index=False)