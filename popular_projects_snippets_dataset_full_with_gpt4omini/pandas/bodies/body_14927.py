# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_converter.py
# Run in subprocess to ensure a clean state
code = (
    "import matplotlib.units; "
    "import pandas as pd; "
    "units = dict(matplotlib.units.registry); "
    "assert pd.Timestamp not in units"
)
call = [sys.executable, "-c", code]
assert subprocess.check_call(call) == 0
