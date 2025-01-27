# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_conversion.py
from l3.Runtime import _l_
expected = pd.Index(
    (
        ("foo", "one"),
        ("foo", "two"),
        ("bar", "one"),
        ("baz", "two"),
        ("qux", "one"),
        ("qux", "two"),
    ),
    tupleize_cols=False,
)
_l_(21963)
result = idx.to_flat_index()
_l_(21964)
tm.assert_index_equal(result, expected)
_l_(21965)
