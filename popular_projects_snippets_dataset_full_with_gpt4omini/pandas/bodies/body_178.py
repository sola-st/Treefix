# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
df = DataFrame({"dt": ["a", "b", "c", "a"]}, dtype="category")
result = df.apply(lambda x: x)
tm.assert_frame_equal(result, df)
