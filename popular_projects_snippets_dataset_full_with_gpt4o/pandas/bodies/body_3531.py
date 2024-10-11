# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
df = frame_of_index_cols
df.index.name = index_name

keys = ["A", box(df["B"])]
# np.array/list "forget" the name of B
names = ["A", None if box in [np.array, list, tuple, iter] else "B"]

result = df.set_index(keys, drop=drop, append=append)

# only valid column keys are dropped
# since B is always passed as array above, only A is dropped, if at all
expected = df.set_index(["A", "B"], drop=False, append=append)
expected = expected.drop("A", axis=1) if drop else expected
expected.index.names = [index_name] + names if append else names

tm.assert_frame_equal(result, expected)
