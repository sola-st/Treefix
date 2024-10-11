# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH#??? frame.__foo__ should only accept one argument
df = DataFrame({"A": [0.0, 0.0], "B": [0.0, None]})
b = df["B"]
with pytest.raises(TypeError, match="takes 2 positional arguments"):
    getattr(df, all_arithmetic_operators)(b, 0)
