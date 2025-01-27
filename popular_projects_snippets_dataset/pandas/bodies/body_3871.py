# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
df = DataFrame({"year": date_range("1/1/1700", periods=50, freq="A-DEC")})
# it works!
repr(df)
