# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# GH 11149
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
expected = df.copy()

expected["c"] = expected["a"] + expected["b"]
expected["d"] = expected["c"] + expected["b"]
df = df.eval(
    """
        c = a + b
        d = c + b""",
    inplace=False,
)
tm.assert_frame_equal(expected, df)

expected["a"] = expected["a"] - 1
expected["e"] = expected["a"] + 2
df = df.eval(
    """
        a = a - 1
        e = a + 2""",
    inplace=False,
)
tm.assert_frame_equal(expected, df)
