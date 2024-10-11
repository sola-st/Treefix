import pandas as pd # pragma: no cover
import tempfile # pragma: no cover

read_ext = ".xlsx" # pragma: no cover

import pandas as pd # pragma: no cover
import tempfile # pragma: no cover
import os # pragma: no cover

read_ext = '.xlsx' # pragma: no cover
with tempfile.NamedTemporaryFile(suffix=read_ext, delete=False) as tmp:# pragma: no cover
    basename = tmp.name[:-5]# pragma: no cover
    df1 = pd.DataFrame({'Data': [1, 2, 3]})# pragma: no cover
    df2 = pd.DataFrame({'Data': [4, 5, 6]})# pragma: no cover
    df3 = pd.DataFrame({'Data': [7, 8, 9]})# pragma: no cover
class MockTestUtils:# pragma: no cover
    @staticmethod# pragma: no cover
    def assert_contains_all(expected, actual):# pragma: no cover
        for item in expected:# pragma: no cover
            assert item in actual, f'Expected item {item} not found in actual dictionary.'# pragma: no cover
        print('Assertion Passed: All expected items found in actual dictionary keys.') # pragma: no cover
tm = type('Mock', (object,), {'assert_contains_all': MockTestUtils.assert_contains_all}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# Test reading all sheet names by setting sheet_name to None,
# Ensure a dict is returned.
# See PR #9450
from l3.Runtime import _l_
basename = "test_multisheet"
_l_(16584)
dfs = pd.read_excel(basename + read_ext, sheet_name=None)
_l_(16585)
# ensure this is not alphabetical to test order preservation
expected_keys = ["Charlie", "Alpha", "Beta"]
_l_(16586)
tm.assert_contains_all(expected_keys, dfs.keys())
_l_(16587)
# Issue 9930
# Ensure sheet order is preserved
assert expected_keys == list(dfs.keys())
_l_(16588)
