# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
uval = "\u03c3\u03c3\u03c3\u03c3"

df = DataFrame({"A": [uval, uval]})

result = repr(df)
ex_top = "      A"
assert result.split("\n")[0].rstrip() == ex_top

df = DataFrame({"A": [uval, uval]})
result = repr(df)
assert result.split("\n")[0].rstrip() == ex_top
