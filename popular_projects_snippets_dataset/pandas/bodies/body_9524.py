# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_reduction.py
op = all_numeric_reductions
s = pd.Series(data)
if dropna:
    s = s.dropna()

if op in ("sum", "prod"):
    assert isinstance(getattr(s, op)(), np.int_)
elif op == "count":
    # Oddly on the 32 bit build (but not Windows), this is intc (!= intp)
    assert isinstance(getattr(s, op)(), np.integer)
elif op in ("min", "max"):
    assert isinstance(getattr(s, op)(), np.bool_)
else:
    # "mean", "std", "var", "median", "kurt", "skew"
    assert isinstance(getattr(s, op)(), np.float64)
