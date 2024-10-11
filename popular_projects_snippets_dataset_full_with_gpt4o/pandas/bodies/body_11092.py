# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH15072
grouped = df.groupby("A", as_index=False)
msg = r"Column\(s\) C already selected"

with pytest.raises(IndexError, match=msg):
    grouped["C"].__getitem__("D")
