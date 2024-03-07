import sys
import atexit

from .CoverageManager import CoverageManager


file = sys.argv[0]
predictor = sys.argv[1]

coverage_manager = CoverageManager()
atexit.register(coverage_manager.save, file, predictor)

def _l_(iid):
    if coverage_manager is not None:
        coverage_manager.cover_line(iid)
        coverage_manager.save(file, predictor)