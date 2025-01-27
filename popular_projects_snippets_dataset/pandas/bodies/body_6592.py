# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_setops.py
# GH#12034 Cases where we operate against another RangeIndex and may
#  get back another RangeIndex
obj = RangeIndex.from_range(range(1, 10), name="foo")

result = obj.difference(obj)
expected = RangeIndex.from_range(range(0), name="foo")
tm.assert_index_equal(result, expected, exact=True)

result = obj.difference(expected.rename("bar"))
tm.assert_index_equal(result, obj.rename(None), exact=True)

result = obj.difference(obj[:3])
tm.assert_index_equal(result, obj[3:], exact=True)

result = obj.difference(obj[-3:])
tm.assert_index_equal(result, obj[:-3], exact=True)

# Flipping the step of 'other' doesn't affect the result, but
#  flipping the stepof 'self' does when sort=None
result = obj[::-1].difference(obj[-3:])
tm.assert_index_equal(result, obj[:-3], exact=True)

result = obj[::-1].difference(obj[-3:], sort=False)
tm.assert_index_equal(result, obj[:-3][::-1], exact=True)

result = obj[::-1].difference(obj[-3:][::-1])
tm.assert_index_equal(result, obj[:-3], exact=True)

result = obj[::-1].difference(obj[-3:][::-1], sort=False)
tm.assert_index_equal(result, obj[:-3][::-1], exact=True)

result = obj.difference(obj[2:6])
expected = Index([1, 2, 7, 8, 9], name="foo")
tm.assert_index_equal(result, expected, exact=True)
