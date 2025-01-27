# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH 11565
df = DataFrame(
    {x: {"x": "foo", "y": "bar", "z": "baz"} for x in ["a", "b", "c"]}
)

f = getattr(operator, compare_operators_no_eq_ne)
msg = "'[<>]=?' not supported between instances of 'str' and 'int'"
with pytest.raises(TypeError, match=msg):
    f(df, 0)
