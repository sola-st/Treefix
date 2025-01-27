# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
# Regression test for GH#8019
df = DataFrame({"foo": []})
rs = df.shift(-1)

tm.assert_frame_equal(df, rs)
