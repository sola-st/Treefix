import os
import csv
import time
import signal
import subprocess
import pandas as pd

from .Hyperparams import Hyperparams as param


class RuntimeStats:
    def __init__(self):
        self.initial_predictions_indexes = []
        self.refined_predictions_indexes = {}
        self.guide_attempt = 0
        self.guided_predictions_indexes = {}
        self.executed_lines = set()
        self.coverage_percentage = 0

    def measure_coverage(self, file_path, predictor_name):
        # run the file (with a timeout)
        log_file = open(f"{file_path}_execution_log.txt", "w")
        try:
            process = subprocess.Popen(
                f"time python {file_path} {predictor_name}", shell=True, start_new_session=True, stdout=log_file, stderr=log_file)
            process.wait(timeout=30)  # seconds
        except subprocess.TimeoutExpired:
            log_file.write("TimeLimit!!!!")
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)

        project_name = ""
        file_name = file_path.split("/")[2].split('.')[0]

        if os.path.isfile(f'./metrics/{param.dataset}/{predictor_name}/raw/metrics_{project_name}_{file_name}_coverage.pkl'):
            df = pd.read_pickle(f'./metrics/{param.dataset}/{predictor_name}/raw/metrics_{project_name}_{file_name}_coverage.pkl')
            covered_lines = df.iloc[-1]['covered_lines']
            additional_covered_lines = self.executed_lines.difference(covered_lines).union(covered_lines.difference(self.executed_lines))
            self.executed_lines = self.executed_lines.union(additional_covered_lines)
            self.coverage_percentage = len(self.executed_lines)/self.total_lines

    def _save_summary_metrics(self, file, predictor_name, execution_time, prediction_type):
        project_name = ""
        file_name = file.split("/")[2].split('.')[0]

        # Create CSV file and add header if it doesn't exist
        if not os.path.isfile(f'./metrics/{param.dataset}/{predictor_name}/raw/metrics_{project_name}_{file_name}.csv'):
            columns = [
                'file', 'predictor', 'prediction_type', 'execution_time', 
                'initial_predictions_indexes', 'refined_predictions_indexes', 'guide_attempt', 'guided_predictions_indexes',
                'covered_lines', 'num_covered_lines', 'total_lines', 'coverage_percentage'       
            ]

            with open(f'./metrics/{param.dataset}/{predictor_name}/raw/metrics_{project_name}_{file_name}.csv', 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(columns)

        df = pd.read_csv(f'./metrics/{param.dataset}/{predictor_name}/raw/metrics_{project_name}_{file_name}.csv')
        df_new_data = pd.DataFrame({
            'file': [file],
            'predictor': [predictor_name],
            'prediction_type': [prediction_type],
            'execution_time': [execution_time],
            'initial_predictions_indexes': [self.initial_predictions_indexes],
            'refined_predictions_indexes': [self.refined_predictions_indexes],
            'guide_attempt': [self.guide_attempt],
            'guided_predictions_indexes': [self.guided_predictions_indexes],
            'covered_lines': [self.executed_lines],
            'num_covered_lines': [len(self.executed_lines)],
            'total_lines': [self.total_lines],
            'coverage_percentage': [self.coverage_percentage]
        })
        df = pd.concat([df, df_new_data])
        df.to_csv(f'./metrics/{param.dataset}/{predictor_name}/raw/metrics_{project_name}_{file_name}.csv', index=False)

    def save(self, file, predictor_name, start_time, prediction_type):
        self._save_summary_metrics(file, predictor_name, time.time() - start_time, prediction_type)