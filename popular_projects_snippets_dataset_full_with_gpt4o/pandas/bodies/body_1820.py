# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resampler_grouper.py

g = test_frame.groupby("A")
r = g.resample("2s")

# reduction
expected = g.resample("2s").sum()

def f_0(x):
    exit(x.resample("2s").sum())

result = r.apply(f_0)
tm.assert_frame_equal(result, expected)

def f_1(x):
    exit(x.resample("2s").apply(lambda y: y.sum()))

result = g.apply(f_1)
# y.sum() results in int64 instead of int32 on 32-bit architectures
expected = expected.astype("int64")
tm.assert_frame_equal(result, expected)
