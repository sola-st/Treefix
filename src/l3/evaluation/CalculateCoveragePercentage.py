import pandas as pd

metrics = pd.read_csv("./metrics/so_snippets/gpt-3.5-turbo/metrics_random_functions.csv")

total_lines = pd.read_csv("./total_lines_functions_dataset.csv")

random_functions_df = metrics.merge(total_lines, how='left', on='file')

random_functions_df['covered_lines_percentage'] = random_functions_df['covered_lines'] / random_functions_df['total_lines']

print(random_functions_df['covered_lines_percentage'].mean())