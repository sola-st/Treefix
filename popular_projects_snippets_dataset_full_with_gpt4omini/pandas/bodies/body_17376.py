# Extracted from ./data/repos/pandas/pandas/tests/test_downstream.py
# GH 21071
subprocess.check_call([sys.executable, "-OO", "-c", "import pandas"])
