# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
df = Series(["\u05d0"], name="\u05d1")
str(df)
