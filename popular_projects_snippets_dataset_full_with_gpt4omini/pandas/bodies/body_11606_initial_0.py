import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from io import StringIO # pragma: no cover
import pandas.testing as tm # pragma: no cover

all_parsers = pd # pragma: no cover
StringIO = StringIO # pragma: no cover
DataFrame = pd.DataFrame # pragma: no cover
np = np # pragma: no cover
tm = tm # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_empty.py
from l3.Runtime import _l_
parser = all_parsers
_l_(10319)

data = "one,two"
_l_(10320)
result = parser.read_csv(StringIO(data), dtype={"one": "u1"})
_l_(10321)

expected = DataFrame(
    {"one": np.empty(0, dtype="u1"), "two": np.empty(0, dtype=object)},
)
_l_(10322)
tm.assert_frame_equal(result, expected)
_l_(10323)
