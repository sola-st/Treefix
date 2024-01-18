import pandas as pd
import os
from os import path
import csv
import time
from .Logging import logger
from .IIDS import IIDs
from .Hyperparams import Hyperparams as param

write_metrics = True


class RuntimeStats:
    def __init__(self, iids_file):
        self.executed_lines = []
        self.iids = IIDs(iids_file)

    def cover_line(self, iid):
        self.executed_lines.append(iid)
        logger.info(f"Line {self.iids.line(iid)}: Executed")

    def _save_summary_metrics(self, file, predictor_name):
        if write_metrics:
            if param.dataset == "so_snippets":
                project_name = ""
                file_name = file.split("/")[2].split('.')[0]
            else:
                project_name = file.split("/")[2]
                file_name = file.split("/")[4].split('.')[0]

            # Create destination dir if it doesn't exist
            if not os.path.exists('./metrics'):
                os.makedirs('./metrics')
            if not os.path.exists(f'./metrics/{param.dataset}'):
                os.makedirs(f'./metrics/{param.dataset}')
            if not os.path.exists(f'./metrics/{param.dataset}/{predictor_name}'):
                os.makedirs(f'./metrics/{param.dataset}/{predictor_name}')
            if not os.path.exists(f'./metrics/{param.dataset}/{predictor_name}/raw'):
                os.makedirs(f'./metrics/{param.dataset}/{predictor_name}/raw')

            # Create CSV file and add header if it doesn't exist
            if not os.path.isfile(f'./metrics/{param.dataset}/{predictor_name}/raw/metrics_{project_name}_{file_name}.csv'):
                columns = ['file', 'predictor', 'executed_lines', 'covered_lines']

                with open(f'./metrics/{param.dataset}/{predictor_name}/raw/metrics_{project_name}_{file_name}.csv', 'a') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(columns)

            df = pd.read_csv(f'./metrics/{param.dataset}/{predictor_name}/raw/metrics_{project_name}_{file_name}.csv')
            df_new_data = pd.DataFrame({
                'file': [file],
                'predictor': [predictor_name],
                'executed_lines': [len(self.executed_lines)],
                'covered_lines': [len(set(self.executed_lines))]
            })
            df = pd.concat([df, df_new_data])
            df.to_csv(f'./metrics/{param.dataset}/{predictor_name}/raw/metrics_{project_name}_{file_name}.csv', index=False)
            print("saved")

    def save(self, file, predictor_name="gpt-3.5-turbo"):
        self._save_summary_metrics(file, predictor_name)