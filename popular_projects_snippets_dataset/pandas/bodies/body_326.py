# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# GH 11149
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
expected = df.copy()

expected["c"] = expected["a"] + expected["b"]
expected["d"] = expected["c"] + expected["b"]
answer = df.eval(
    """
        c = a + b
        d = c + b""",
    inplace=True,
)
tm.assert_frame_equal(expected, df)
assert answer is None

expected["a"] = expected["a"] - 1
expected["e"] = expected["a"] + 2
answer = df.eval(
    """
        a = a - 1
        e = a + 2""",
    inplace=True,
)
tm.assert_frame_equal(expected, df)
assert answer is None

# multi-line not valid if not all assignments
msg = "Multi-line expressions are only valid if all expressions contain"
with pytest.raises(ValueError, match=msg):
    df.eval(
        """
            a = b + 2
            b - 2""",
        inplace=False,
    )
