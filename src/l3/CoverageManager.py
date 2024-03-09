import os
import pandas as pd

from .Util import count_lines
from .Hyperparams import Hyperparams as param


class CoverageManager:
    def __init__(self):
        self.executed_lines = set()

    def cover_line(self, iid):
        self.executed_lines.add(iid)

    def _save_metrics(self, file, predictor_name):
        project_name = ""
        file_name = file.split("/")[2].split('.')[0]
        total_lines = count_lines(file)
        
        if not os.path.isfile(f'./metrics/{param.dataset}/{predictor_name}/raw/metrics_{project_name}_{file_name}_coverage.pkl'):
            columns = ('file', 'predictor', 'covered_lines', 'num_covered_lines', 'total_lines', 'coverage_percentage')
            df = pd.DataFrame(columns = columns)
        else:
            df = pd.read_pickle(f'./metrics/{param.dataset}/{predictor_name}/raw/metrics_{project_name}_{file_name}_coverage.pkl')

        df_new_data = pd.DataFrame({
            'file': [file],
            'predictor': [predictor_name],
            'covered_lines': [self.executed_lines],
            'num_covered_lines': [len(self.executed_lines)],
            'total_lines': [total_lines],
            'coverage_percentage': [len(self.executed_lines)/total_lines]
        })
        df = pd.concat([df, df_new_data])
        df.to_pickle(f'./metrics/{param.dataset}/{predictor_name}/raw/metrics_{project_name}_{file_name}_coverage.pkl')


    def save(self, file, predictor_name):
        self._save_metrics(file, predictor_name)
