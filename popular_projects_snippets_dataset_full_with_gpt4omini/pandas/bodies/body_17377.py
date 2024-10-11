# Extracted from ./data/repos/pandas/pandas/tests/test_downstream.py
# GH 42866
subprocess.check_call(
    [
        sys.executable,
        "-OO",
        "-c",
        (
            "import pandas as pd, pickle; "
            "pickle.loads(pickle.dumps(pd.date_range('2021-01-01', periods=1)))"
        ),
    ]
)
