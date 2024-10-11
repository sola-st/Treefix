# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH4968
# invalid date/int comparisons
x = DataFrame(arg)
y = DataFrame(arg2)
# we expect the result to match Series comparisons for
# == and !=, inequalities should raise
result = x == y
expected = DataFrame(
    {col: x[col] == y[col] for col in x.columns},
    index=x.index,
    columns=x.columns,
)
tm.assert_frame_equal(result, expected)

result = x != y
expected = DataFrame(
    {col: x[col] != y[col] for col in x.columns},
    index=x.index,
    columns=x.columns,
)
tm.assert_frame_equal(result, expected)

msgs = [
    r"Invalid comparison between dtype=datetime64\[ns\] and ndarray",
    "invalid type promotion",
    (
        # npdev 1.20.0
        r"The DTypes <class 'numpy.dtype\[.*\]'> and "
        r"<class 'numpy.dtype\[.*\]'> do not have a common DType."
    ),
]
msg = "|".join(msgs)
with pytest.raises(TypeError, match=msg):
    x >= y
with pytest.raises(TypeError, match=msg):
    x > y
with pytest.raises(TypeError, match=msg):
    x < y
with pytest.raises(TypeError, match=msg):
    x <= y
