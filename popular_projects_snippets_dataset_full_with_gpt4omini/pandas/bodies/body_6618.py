# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
i = RangeIndex(5, name="Foo")
result = repr(i)
expected = "RangeIndex(start=0, stop=5, step=1, name='Foo')"
assert result == expected

result = eval(result)
tm.assert_index_equal(result, i, exact=True)

i = RangeIndex(5, 0, -1)
result = repr(i)
expected = "RangeIndex(start=5, stop=0, step=-1)"
assert result == expected

result = eval(result)
tm.assert_index_equal(result, i, exact=True)
