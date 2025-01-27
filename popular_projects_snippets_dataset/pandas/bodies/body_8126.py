# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# Check that "name" argument passed at initialization is honoured
# GH12309
index = simple_index

first = type(index)(index, copy=True, name="mario")
second = type(first)(first, copy=False)

# Even though "copy=False", we want a new object.
assert first is not second
tm.assert_index_equal(first, second)

assert first.name == "mario"
assert second.name == "mario"

s1 = Series(2, index=first)
s2 = Series(3, index=second[:-1])

s3 = s1 * s2

assert s3.index.name == "mario"
