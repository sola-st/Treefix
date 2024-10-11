import pandas as pd # pragma: no cover
from pandas import DataFrame # pragma: no cover
import pandas.testing as tm # pragma: no cover
import tempfile # pragma: no cover
import os # pragma: no cover

path = os.path.join(tempfile.gettempdir(), 'test.xlsx') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# Test for issue #5427.
from l3.Runtime import _l_
write_frame = DataFrame({"A": [1, 1, 1], "B": [2, 2, 2]})
_l_(19051)
write_frame.to_excel(path, "test1", columns=["B", "A"])
_l_(19052)

read_frame = pd.read_excel(path, sheet_name="test1", header=0)
_l_(19053)

tm.assert_series_equal(write_frame["A"], read_frame["A"])
_l_(19054)
tm.assert_series_equal(write_frame["B"], read_frame["B"])
_l_(19055)
