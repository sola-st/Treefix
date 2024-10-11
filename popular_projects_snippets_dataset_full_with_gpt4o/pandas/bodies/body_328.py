# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# GH 15342
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
expected = df.copy()

local_var = 7
expected["c"] = expected["a"] * local_var
expected["d"] = expected["c"] + local_var
answer = df.eval(
    """
        c = a * @local_var
        d = c + @local_var
        """,
    inplace=True,
)
tm.assert_frame_equal(expected, df)
assert answer is None
