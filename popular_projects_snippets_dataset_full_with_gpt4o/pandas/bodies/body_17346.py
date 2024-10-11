# Extracted from ./data/repos/pandas/pandas/tests/generic/test_label_or_level_utils.py
"""DataFrame with levels 'L1' and 'L2' and labels 'L1' and 'L3'"""
df = df.set_index(["L1", "L2"])

df["L1"] = df["L3"]

exit(df)
