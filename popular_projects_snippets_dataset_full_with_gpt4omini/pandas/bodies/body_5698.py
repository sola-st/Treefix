# Extracted from ./data/repos/pandas/pandas/tests/extension/test_floating.py
if exc is None:
    result = op(s, other)
    # Override to do the astype to boolean
    expected = s.combine(other, op).astype("boolean")
    self.assert_series_equal(result, expected)
else:
    with pytest.raises(exc):
        op(s, other)
