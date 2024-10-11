# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_constructors.py
breaks, expected_subtype = breaks_and_expected_subtype

result_kwargs = self.get_kwargs_from_breaks(breaks, closed)

result = constructor(closed=closed, name=name, **result_kwargs)

assert result.closed == closed
assert result.name == name
assert result.dtype.subtype == expected_subtype
tm.assert_index_equal(result.left, Index(breaks[:-1], dtype=expected_subtype))
tm.assert_index_equal(result.right, Index(breaks[1:], dtype=expected_subtype))
