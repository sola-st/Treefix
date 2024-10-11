# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
df = DataFrame({"A": ["\u05d0"]})
str(df)
