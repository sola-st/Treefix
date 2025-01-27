# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_floats.py
"""make sure that we are raising on positional indexing
        w.r.t. an integer index
        """
s = Series(range(2, 6), index=range(2, 6))

result = s[2:4]
expected = s.iloc[2:4]
tm.assert_series_equal(result, expected)

klass = RangeIndex
msg = (
    "cannot do (slice|positional) indexing "
    rf"on {klass.__name__} with these indexers \[(2|4)\.0\] of "
    "type float"
)
with pytest.raises(TypeError, match=msg):
    s[idx]
with pytest.raises(TypeError, match=msg):
    s.iloc[idx]
