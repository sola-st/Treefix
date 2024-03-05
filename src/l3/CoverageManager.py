import os
import csv
import time
import pandas as pd

from .IIDS import IIDs
from .Hyperparams import Hyperparams as param

class CoverageManager:
    def __init__(self):
        self.executed_lines = set()
        self.iids = IIDs(param.iids_file)

    def cover_line(self, iid):
        self.executed_lines.add(iid)

    def count_lines(self, file_path):
        total_lines = 0
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line.startswith("_l_("):
                    total_lines += 1
        return total_lines
    
    def _save_metrics(self, file, predictor_name, execution_time):
        project_name = ""
        file_name = file.split("/")[2].split('.')[0]
        
        # Create CSV file and add header if it doesn't exist
        if not os.path.isfile(f'./metrics/{param.dataset}/{predictor_name}/raw/metrics_{project_name}_{file_name}_coverage.csv'):
            columns = ['file', 'predictor', 'execution_time', 'covered_lines', 'total_lines', 'coverage_percentage']

            with open(f'./metrics/{param.dataset}/{predictor_name}/raw/metrics_{project_name}_{file_name}_coverage.csv', 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(columns)

        df = pd.read_csv(f'./metrics/{param.dataset}/{predictor_name}/raw/metrics_{project_name}_{file_name}_coverage.csv')
        df_new_data = pd.DataFrame({
            'file': [file],
            'predictor': [predictor_name],
            'execution_time': [execution_time],
            'covered_lines': [len(self.executed_lines)],
            'total_lines': [self.total_lines],
            'coverage_percentage': [len(self.executed_lines)/self.total_lines]
        })
        df = pd.concat([df, df_new_data])
        df.to_csv(f'./metrics/{param.dataset}/{predictor_name}/raw/metrics_{project_name}_{file_name}_coverage.csv', index=False)

    def save(self, file, predictor_name, start_time):
        self._save_metrics(file, predictor_name, time.time() - start_time)
