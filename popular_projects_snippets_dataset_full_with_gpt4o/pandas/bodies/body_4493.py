# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
series = float_frame._series

df = DataFrame({"A": series["A"]}, copy=True)
# TODO can be replaced with `df.loc[:, "A"] = 5` after deprecation about
# inplace mutation is enforced
df.loc[df.index[0] : df.index[-1], "A"] = 5

assert not (series["A"] == 5).all()
