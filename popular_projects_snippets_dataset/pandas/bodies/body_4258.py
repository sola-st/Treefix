# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH 15697, GH 22163 df.eq(pd.NaT) should behave like df == pd.NaT,
# and _definitely_ not be NaN
df = DataFrame([pd.NaT])

result = df == pd.NaT
# result.iloc[0, 0] is a np.bool_ object
assert result.iloc[0, 0].item() is False

result = df.eq(pd.NaT)
assert result.iloc[0, 0].item() is False

result = df != pd.NaT
assert result.iloc[0, 0].item() is True

result = df.ne(pd.NaT)
assert result.iloc[0, 0].item() is True
