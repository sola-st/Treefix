# Extracted from ./data/repos/pandas/pandas/tests/window/test_ewm.py
# GH#42452

df = DataFrame(
    {0: range(5), 1: range(6, 11), 2: range(10, 20, 2)}, dtype=float_numpy_dtype
)
e = df.ewm(alpha=0.5, axis=1)
result = getattr(e, func)()

tm.assert_frame_equal(result, expected)
