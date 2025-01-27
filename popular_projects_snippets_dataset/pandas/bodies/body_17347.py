# Extracted from ./data/repos/pandas/pandas/tests/generic/test_label_or_level_utils.py
"""DataFrame with level 'L1' and labels 'L2', 'L3', and 'L2'"""
df = df.set_index(["L1"])
df = pd.concat([df, df["L2"]], axis=1)

exit(df)
