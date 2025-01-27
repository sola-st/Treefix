# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
# GH 47649
pdf = DataFrame(
    {
        ("x", "a"): [np.nan, 2.0, 3.0],
        ("x", "b"): [1.0, 2.0, np.nan],
        ("y", "c"): [1.0, 2.0, np.nan],
    }
)
expected = DataFrame(
    {
        ("x", "a"): [-1.0, 2.0, 3.0],
        ("x", "b"): [1.0, 2.0, -1.0],
        ("y", "c"): [1.0, 2.0, np.nan],
    }
)
tm.assert_frame_equal(pdf.fillna({"x": -1}), expected)
tm.assert_frame_equal(pdf.fillna({"x": -1, ("x", "b"): -2}), expected)

expected = DataFrame(
    {
        ("x", "a"): [-1.0, 2.0, 3.0],
        ("x", "b"): [1.0, 2.0, -2.0],
        ("y", "c"): [1.0, 2.0, np.nan],
    }
)
tm.assert_frame_equal(pdf.fillna({("x", "b"): -2, "x": -1}), expected)
