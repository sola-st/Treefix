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
    
        files = [file for file in files if file.startswith("metrics_") and file.endswith(".csv")]

        combined_df_for_predictor = pd.DataFrame()

        for file in files:
            try:
                df = pd.read_csv(f'{folder_path}{dataset}/{predictor}/raw/{file}')
                df_aux = pd.DataFrame(columns=df.columns)
                df_aux = pd.concat([df_aux, df[df['prediction_type'] == 'initial'].head(1)])
                df_aux = pd.concat([df_aux, df[df['prediction_type'] == 'refine'].head(1)])
                df_aux = pd.concat([df_aux, df[df['prediction_type'] == 'guide'].head(1)])
                combined_df_for_predictor = pd.concat([combined_df_for_predictor, df_aux], ignore_index=True)

            except pd.errors.EmptyDataError:
                print(file)

        combined_df_for_predictor.to_csv(f'{folder_path}metrics_{dataset}_dataset.csv', index=False)

        combined_df_for_dataset = pd.concat([combined_df_for_dataset, combined_df_for_predictor], ignore_index=True)

        combined_df_for_predictor_grouped = combined_df_for_predictor.groupby(by="prediction_type", as_index=False)[["coverage_percentage", "max_coverage_prediction_value"]].mean()

        combined_df_for_predictor_grouped.to_csv(f'{folder_path}metrics_{dataset}_dataset_grouped.csv', index=False)
