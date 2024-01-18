import atexit
import sys
from l3.RuntimeStats import RuntimeStats

file = sys.argv[0]
iids = sys.argv[1]

runtime_stats = RuntimeStats(iids)
atexit.register(runtime_stats.save, file)

def _l_(iid):
    if runtime_stats is not None:
        runtime_stats.cover_line(iid)
        runtime_stats.save(file)