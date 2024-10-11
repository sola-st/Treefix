# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_setops.py
index = monotonic_index(0, 11, closed=closed)
set_op = getattr(index, op_name)

# TODO: standardize return type of non-union setops type(self vs other)
# non-IntervalIndex
if op_name == "difference":
    expected = index
else:
    expected = getattr(index.astype("O"), op_name)(Index([1, 2, 3]))
result = set_op(Index([1, 2, 3]), sort=sort)
tm.assert_index_equal(result, expected)

# mixed closed -> cast to object
for other_closed in {"right", "left", "both", "neither"} - {closed}:
    other = monotonic_index(0, 11, closed=other_closed)
    expected = getattr(index.astype(object), op_name)(other, sort=sort)
    if op_name == "difference":
        expected = index
    result = set_op(other, sort=sort)
    tm.assert_index_equal(result, expected)

# GH 19016: incompatible dtypes -> cast to object
other = interval_range(Timestamp("20180101"), periods=9, closed=closed)
expected = getattr(index.astype(object), op_name)(other, sort=sort)
if op_name == "difference":
    expected = index
result = set_op(other, sort=sort)
tm.assert_index_equal(result, expected)
