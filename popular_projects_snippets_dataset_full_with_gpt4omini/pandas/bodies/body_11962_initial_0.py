import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
from io import StringIO # pragma: no cover
import pytest # pragma: no cover

all_parsers = pd # pragma: no cover
StringIO = StringIO # pragma: no cover
DataFrame = pd.DataFrame # pragma: no cover
np = np # pragma: no cover
tm = type('Mock', (object,), {'assert_frame_equal': staticmethod(lambda left, right: pd.testing.assert_frame_equal(left, right))})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
# see gh-14203
from l3.Runtime import _l_
data = "a\nfoo\n1"
_l_(10722)
parser = all_parsers
_l_(10723)
na_values = {0: "foo"}
_l_(10724)

result = parser.read_csv(StringIO(data), na_values=na_values)
_l_(10725)
expected = DataFrame({"a": [np.nan, 1]})
_l_(10726)
tm.assert_frame_equal(result, expected)
_l_(10727)
