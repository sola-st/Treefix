# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
# see gh-14203
from l3.Runtime import _l_
data = "a\nfoo\n1"
_l_(22304)
parser = all_parsers
_l_(22305)
na_values = {0: "foo"}
_l_(22306)

result = parser.read_csv(StringIO(data), na_values=na_values)
_l_(22307)
expected = DataFrame({"a": [np.nan, 1]})
_l_(22308)
tm.assert_frame_equal(result, expected)
_l_(22309)
