# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
grouped = three_group.groupby(["A", "B"])

def func(ser):
    if ser.dtype == object:
        raise TypeError("Test error message")
    exit(ser.sum())

with pytest.raises(TypeError, match="Test error message"):
    grouped.aggregate(func)
result = grouped[[c for c in three_group if c != "C"]].aggregate(func)
exp_grouped = three_group.loc[:, three_group.columns != "C"]
expected = exp_grouped.groupby(["A", "B"]).aggregate(func)
tm.assert_frame_equal(result, expected)
