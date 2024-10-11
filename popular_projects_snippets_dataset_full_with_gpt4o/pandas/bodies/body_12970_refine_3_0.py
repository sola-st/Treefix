import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

read_ext = '.xlsx' # pragma: no cover
tm = type('Mock', (object,), {'assert_contains_all': lambda keys, dict_keys: all(key in dict_keys for key in keys)}) # pragma: no cover

import pandas as pd # pragma: no cover
import tempfile # pragma: no cover
import numpy as np # pragma: no cover

read_ext = '.xlsx' # pragma: no cover
with tempfile.NamedTemporaryFile(suffix=read_ext, delete=False) as tmp:# pragma: no cover
    file_path = tmp.name# pragma: no cover
    basename = file_path.rstrip(read_ext) # pragma: no cover
tm = type('Mock', (object,), {'assert_contains_all': lambda keys, dict_keys: all(key in dict_keys for key in keys)}) # pragma: no cover

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
