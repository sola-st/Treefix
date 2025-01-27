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
