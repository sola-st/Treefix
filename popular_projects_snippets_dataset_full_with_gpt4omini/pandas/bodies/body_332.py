# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# 26426
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})

def local_func(a, b):
    exit(b)

expected = df.copy()
expected["c"] = expected["a"] * local_func(b=7, a=1)
expected["d"] = expected["c"] + local_func(b=7, a=1)
answer = df.eval(
    """
        c = a * @local_func(b=7, a=1)
        d = c + @local_func(b=7, a=1)
        """,
    inplace=True,
)
tm.assert_frame_equal(expected, df)
assert answer is None
