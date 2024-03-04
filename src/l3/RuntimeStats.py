import os
import csv
import time
import pandas as pd


class RuntimeStats:
    def __init__(self):
        self.prediction_index = 0
        self.refine_attempt = 0
        self.refined_prediction_index = 0
        self.executed_lines = []

    def cover_line(self, iid):
        self.executed_lines.append(iid)

    def _save_summary_metrics(self, file, predictor_name, execution_time):
        # Create CSV file and add header if it doesn't exist
        if not os.path.isfile(f'./metrics/additional_metrics_functions.csv'):
            columns = ['file', 'execution_time', 'prediction_index', 'refine_attempt', 'refined_prediction_index']

            with open(f'./metrics/additional_metrics_functions.csv', 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(columns)

        df = pd.read_csv(f'./metrics/additional_metrics_functions.csv')
        df_new_data = pd.DataFrame({
            'file': [file],
            'predictor': [predictor_name],
            'execution_time': [execution_time],
            'prediction_index': [self.prediction_index],
            'refine_attempt': [self.refine_attempt],
            'refined_prediction_index': [self.refined_prediction_index]
        })
        df = pd.concat([df, df_new_data])
        df.to_csv(f'./metrics/additional_metrics_functions.csv', index=False)

    def save(self, file, predictor_name, start_time):
        self._save_summary_metrics(file, predictor_name, time.time() - start_time)