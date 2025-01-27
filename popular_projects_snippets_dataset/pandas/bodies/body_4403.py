# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
d = {"Col1": {"Row1": "A String", "Row2": np.nan}}
df = DataFrame(d)
assert isinstance(df["Col1"]["Row2"], float)
