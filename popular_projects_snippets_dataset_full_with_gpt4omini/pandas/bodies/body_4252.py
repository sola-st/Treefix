# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
df = DataFrame([{"a": 1, "b": "foo"}, {"a": 2, "b": "bar"}])
mask_a = df.a > 1
tm.assert_frame_equal(df[mask_a], df.loc[1:1, :])
tm.assert_frame_equal(df[-mask_a], df.loc[0:0, :])

mask_b = df.b == "foo"
tm.assert_frame_equal(df[mask_b], df.loc[0:0, :])
tm.assert_frame_equal(df[-mask_b], df.loc[1:1, :])
