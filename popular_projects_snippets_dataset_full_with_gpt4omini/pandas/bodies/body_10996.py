# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# Low level tinkering could be unsafe, make sure not
df = DataFrame({"key": [1, 1, 1, 2, 2, 2, 3, 3, 3], "value": range(9)})

result = df.groupby("key", group_keys=group_keys).apply(lambda x: x.iloc[:2])
expected = df.take([0, 1, 3, 4, 6, 7])
if group_keys:
    expected.index = MultiIndex.from_arrays(
        [[1, 1, 2, 2, 3, 3], expected.index], names=["key", None]
    )

tm.assert_frame_equal(result, expected)
