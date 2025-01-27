# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_setops.py
obj = RangeIndex.from_range(range(1, 10), name="foo")

result = obj.difference(obj[::2])
expected = obj[1::2]
tm.assert_index_equal(result, expected, exact=True)

result = obj[::-1].difference(obj[::2], sort=False)
tm.assert_index_equal(result, expected[::-1], exact=True)

result = obj.difference(obj[1::2])
expected = obj[::2]
tm.assert_index_equal(result, expected, exact=True)

result = obj[::-1].difference(obj[1::2], sort=False)
tm.assert_index_equal(result, expected[::-1], exact=True)
