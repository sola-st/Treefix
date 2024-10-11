# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
df = frame_of_index_cols
keys = MultiIndex.from_arrays([df["A"], df["B"]], names=["A", "B"])

result = df.set_index(keys, drop=drop, append=append)

# setting with a MultiIndex will never drop columns
expected = df.set_index(["A", "B"], drop=False, append=append)

tm.assert_frame_equal(result, expected)
