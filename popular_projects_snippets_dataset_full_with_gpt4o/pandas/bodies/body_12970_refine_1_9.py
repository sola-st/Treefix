import pandas as pd # pragma: no cover
import tempfile # pragma: no cover

read_ext = ".xlsx" # pragma: no cover

import pandas as pd # pragma: no cover
import tempfile # pragma: no cover
import os # pragma: no cover

read_ext = ".xlsx" # pragma: no cover
data = {# pragma: no cover
    'Charlie': pd.DataFrame({'A': [1, 2], 'B': [3, 4]}),# pragma: no cover
    'Alpha': pd.DataFrame({'A': [5, 6], 'B': [7, 8]}),# pragma: no cover
    'Beta': pd.DataFrame({'A': [9, 10], 'B': [11, 12]})# pragma: no cover
}# pragma: no cover
# pragma: no cover
with tempfile.NamedTemporaryFile(delete=False, suffix=read_ext) as tmp:# pragma: no cover
    basename = tmp.name[:-5]  # Remove the ".xlsx" extension from the file name# pragma: no cover
tm = type('Mock', (object,), {'assert_contains_all': lambda expected, actual: all(k in actual for k in expected)}) # pragma: no cover

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
