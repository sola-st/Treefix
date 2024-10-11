import pandas as pd # pragma: no cover
import pandas.testing as tm # pragma: no cover

read_ext = '.xlsx' # pragma: no cover
tm = type('Mock', (object,), {'assert_contains_all': lambda self, expected, actual: all(item in actual for item in expected)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# Test reading all sheet names by setting sheet_name to None,
# Ensure a dict is returned.
# See PR #9450
from l3.Runtime import _l_
basename = "test_multisheet"
_l_(4989)
dfs = pd.read_excel(basename + read_ext, sheet_name=None)
_l_(4990)
# ensure this is not alphabetical to test order preservation
expected_keys = ["Charlie", "Alpha", "Beta"]
_l_(4991)
tm.assert_contains_all(expected_keys, dfs.keys())
_l_(4992)
# Issue 9930
# Ensure sheet order is preserved
assert expected_keys == list(dfs.keys())
_l_(4993)
