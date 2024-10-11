# Extracted from ./data/repos/pandas/pandas/tests/generic/test_label_or_level_utils.py

# Make series with L1 as index
s = df.set_index("L1").L2
assert_level_values(s, ["L1"], axis=0)

# Make series with L1 and L2 as index
s = df.set_index(["L1", "L2"]).L3
assert_level_values(s, ["L1", "L2"], axis=0)
