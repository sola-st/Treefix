# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py

data = Series(np.arange(9) // 3, index=np.arange(9), dtype=dtype)

index = np.arange(9)
np.random.shuffle(index)
data = data.reindex(index)

grouped = data.groupby(lambda x: x // 3, group_keys=False)

for k, v in grouped:
    assert len(v) == 3

agged = grouped.aggregate(np.mean)
assert agged[1] == 1

tm.assert_series_equal(agged, grouped.agg(np.mean))  # shorthand
tm.assert_series_equal(agged, grouped.mean())
tm.assert_series_equal(grouped.agg(np.sum), grouped.sum())

expected = grouped.apply(lambda x: x * x.sum())
transformed = grouped.transform(lambda x: x * x.sum())
assert transformed[7] == 12
tm.assert_series_equal(transformed, expected)

value_grouped = data.groupby(data)
tm.assert_series_equal(
    value_grouped.aggregate(np.mean), agged, check_index_type=False
)

# complex agg
agged = grouped.aggregate([np.mean, np.std])

msg = r"nested renamer is not supported"
with pytest.raises(SpecificationError, match=msg):
    grouped.aggregate({"one": np.mean, "two": np.std})

group_constants = {0: 10, 1: 20, 2: 30}
agged = grouped.agg(lambda x: group_constants[x.name] + x.mean())
assert agged[1] == 21

# corner cases
msg = "Must produce aggregated value"
# exception raised is type Exception
with pytest.raises(Exception, match=msg):
    grouped.aggregate(lambda x: x * 2)
