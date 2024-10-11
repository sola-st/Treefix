# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_update.py
d = {"a": Series([1, 2, 3, 4]), "b": Series([5, 6, 7, 8])}
df = DataFrame(d)

d["a"] = Series([5, 6, 7, 8])
df.update(d)

expected = DataFrame(d)

tm.assert_frame_equal(df, expected)

d = {"a": [1, 2, 3, 4], "b": [5, 6, 7, 8]}
df = DataFrame(d)

d["a"] = [5, 6, 7, 8]
df.update(d)

expected = DataFrame(d)

tm.assert_frame_equal(df, expected)
