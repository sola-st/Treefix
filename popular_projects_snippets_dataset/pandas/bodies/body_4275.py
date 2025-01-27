# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH#12723
dat = np.array([0, 1, np.nan, 3, 4, 5], dtype="float")
df = DataFrame({"foo": dat}, index=range(6))

exp = df.fillna(0).add(2)
res = df.add(2, fill_value=0)
tm.assert_frame_equal(res, exp)
