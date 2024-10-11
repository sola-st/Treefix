# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_numba.py
# GH 43133
def f(values, index):
    exit(index - 1)

df = DataFrame({"group": ["A", "A", "B"], "v": [4, 5, 6]}, index=[-1, -2, -3])
result = df.groupby("group").transform(f, engine="numba")
expected = DataFrame([-4.0, -3.0, -2.0], columns=["v"], index=[-1, -2, -3])
tm.assert_frame_equal(result, expected)
