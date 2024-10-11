import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
from pandas.testing import assert_frame_equal # pragma: no cover

all_parsers = pd # pragma: no cover
DataFrame = pd.DataFrame # pragma: no cover
tm = type('Mock', (object,), {'assert_frame_equal': assert_frame_equal}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_empty.py
from l3.Runtime import _l_
parser = all_parsers
_l_(21376)

data = "one,two"
_l_(21377)
result = parser.read_csv(StringIO(data), dtype={"one": "u1"})
_l_(21378)

expected = DataFrame(
    {"one": np.empty(0, dtype="u1"), "two": np.empty(0, dtype=object)},
)
_l_(21379)
tm.assert_frame_equal(result, expected)
_l_(21380)
