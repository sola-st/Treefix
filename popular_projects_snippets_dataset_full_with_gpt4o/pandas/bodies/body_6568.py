# Extracted from ./data/repos/pandas/pandas/tests/test_common.py
version = Version(pd.__version__)
try:
    version > Version("0.0.1")
except TypeError:
    raise ValueError(
        "No git tags exist, please sync tags between upstream and your repo"
    )
