import os
import csv
import time
import signal
import subprocess
import pandas as pd

from .Hyperparams import Hyperparams as param


class RuntimeStats:
    def __init__(self, predictor):
        self.initial_predictions_indexes = []
        self.refined_predictions_indexes = {}
        self.guide_attempt = 0
        self.guided_predictions_indexes = {}
        self.executed_lines = set()
        self.coverage_percentage = 0

        self.minimal_predictions_set = []
        self.max_coverage_prediction = ""
        self.max_coverage_prediction_value = 0

        self.out_dir = f'./metrics/{param.dataset}/{predictor.__class__.__name__}/raw/'
        if not os.path.exists(self.out_dir):
            os.makedirs(self.out_dir)

    def measure_coverage(self, file_path, predictor_name, prompt_type, index=0, prediction_index=0):
        # run the file (with a timeout)
        log_file = open(f"{file_path}_execution_log.txt", "w")
        try:
            process = subprocess.Popen(
                f"time python {file_path} {predictor_name}", shell=True, start_new_session=True, stdout=log_file, stderr=log_file)
            process.wait(timeout=30)  # seconds

            if not process.returncode:
                if prompt_type == 2:
                    self.refined_predictions_indexes[index].append(prediction_index)
                elif prompt_type == 3:
                    self.guided_predictions_indexes[index].append(prediction_index)
        except subprocess.TimeoutExpired:
            log_file.write("TimeLimit!!!!")
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)

        if param.dataset == "random_functions":
            project_name = file_path.split("/")[2]
        else:
            project_name = ""
        file_name = file_path.split("/")[-1].split('.')[0]

        if os.path.isfile(f'{self.out_dir}metrics_{project_name}_{file_name}_coverage.pkl'):
            try:
                df = pd.read_pickle(f'{self.out_dir}metrics_{project_name}_{file_name}_coverage.pkl')
                covered_lines = df.iloc[-1]['covered_lines']
                additional_covered_lines = covered_lines.difference(self.executed_lines)
                self.executed_lines = self.executed_lines.union(additional_covered_lines)
                self.coverage_percentage = len(self.executed_lines)/self.total_lines

                if len(additional_covered_lines):
                    self.minimal_predictions_set.append(file_name)
                    if len(covered_lines)/self.total_lines > self.max_coverage_prediction_value:
                        self.max_coverage_prediction = file_name
                        self.max_coverage_prediction_value = len(covered_lines)/self.total_lines

            except EOFError:
                pass

    def _save_summary_metrics(self, file, predictor_name, execution_time, num_executions, prediction_type):
        if param.dataset == "random_functions":
            project_name = file.split("/")[2]
        else:
            project_name = ""
        file_name = file.split("/")[-1].split('.')[0]

        # Create CSV file and add header if it doesn't exist
        if not os.path.isfile(f'{self.out_dir}metrics_{project_name}_{file_name}.csv'):
            columns = [
                'file', 'predictor', 'prediction_type', 'execution_time', 'num_executions',
                'initial_predictions_indexes', 'refined_predictions_indexes', 'guide_attempt', 'guided_predictions_indexes',
                'covered_lines', 'num_covered_lines', 'total_lines', 'coverage_percentage', 
                'minimal_predictions_set', 'minimal_predictions_set_size', 'max_coverage_prediction', 'max_coverage_prediction_value'     
            ]

            with open(f'{self.out_dir}metrics_{project_name}_{file_name}.csv', 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(columns)

        avg_exec_time = execution_time / num_executions if num_executions else 0

        df = pd.read_csv(f'{self.out_dir}metrics_{project_name}_{file_name}.csv')
        df_new_data = pd.DataFrame({
            'file': [file],
            'predictor': [predictor_name],
            'prediction_type': [prediction_type],
            'execution_time': [execution_time],
            'num_executions': [num_executions],
            'avg_exec_time': [avg_exec_time],
            'initial_predictions_indexes': [self.initial_predictions_indexes],
            'refined_predictions_indexes': [self.refined_predictions_indexes],
            'guide_attempt': [self.guide_attempt],
            'guided_predictions_indexes': [self.guided_predictions_indexes],
            'covered_lines': [self.executed_lines],
            'num_covered_lines': [len(self.executed_lines)],
            'total_lines': [self.total_lines],
            'coverage_percentage': [self.coverage_percentage],
            'minimal_predictions_set': [self.minimal_predictions_set],
            'minimal_predictions_set_size': [len(self.minimal_predictions_set)],
            'max_coverage_prediction': [self.max_coverage_prediction],
            'max_coverage_prediction_value': [self.max_coverage_prediction_value]

        })
        df = pd.concat([df, df_new_data])
        df.to_csv(f'{self.out_dir}metrics_{project_name}_{file_name}.csv', index=False)

    def save(self, file, predictor_name, start_time, num_executions, prediction_type):
        self._save_summary_metrics(file, predictor_name, time.time() - start_time, num_executions, prediction_type)
