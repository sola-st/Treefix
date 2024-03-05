import atexit
import sys
import time
from .CoverageManager import CoverageManager


file = sys.argv[0]
predictor = sys.argv[1]
start_time = time.time()

coverage_manager = CoverageManager()
coverage_manager.total_lines = coverage_manager.count_lines(file)

def _l_(iid):
    if coverage_manager is not None:
        coverage_manager.cover_line(iid)
        coverage_manager.save(file, predictor, start_time)
