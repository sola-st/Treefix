from io import StringIO # pragma: no cover
import pandas as pd # pragma: no cover
from pandas import DataFrame, Index # pragma: no cover

all_parsers = pd # pragma: no cover
tm = type('Mock', (object,), {'assert_frame_equal': pd.testing.assert_frame_equal}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_index.py
from l3.Runtime import _l_
data = """index,A,B,C,D
foo,2,3,4,5
bar,7,8,9,10
baz,12,13,14,15
qux,12,13,14,15
foo,12,13,14,15
bar,12,13,14,15
"""
_l_(21258)
parser = all_parsers
_l_(21259)
result = parser.read_csv(StringIO(data), index_col=0)
_l_(21260)

expected = DataFrame(
    [
        [2, 3, 4, 5],
        [7, 8, 9, 10],
        [12, 13, 14, 15],
        [12, 13, 14, 15],
        [12, 13, 14, 15],
        [12, 13, 14, 15],
    ],
    columns=["A", "B", "C", "D"],
    index=Index(["foo", "bar", "baz", "qux", "foo", "bar"], name="index"),
)
_l_(21261)
tm.assert_frame_equal(result, expected)
_l_(21262)
