# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH 19522 passing fill_value to frame flex arith methods should
# raise even in the zero-length special cases
ser_len0 = Series([], dtype=object)
df_len0 = DataFrame(columns=["A", "B"])
df = DataFrame([[1, 2], [3, 4]], columns=["A", "B"])

with pytest.raises(NotImplementedError, match="fill_value"):
    df.add(ser_len0, fill_value="E")

with pytest.raises(NotImplementedError, match="fill_value"):
    df_len0.sub(df["A"], axis=None, fill_value=3)
