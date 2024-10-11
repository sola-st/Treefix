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
_l_(10219)
parser = all_parsers
_l_(10220)
result = parser.read_csv(StringIO(data), index_col=0)
_l_(10221)

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
_l_(10222)
tm.assert_frame_equal(result, expected)
_l_(10223)
