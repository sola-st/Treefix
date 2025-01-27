# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
# GH#14353

# Get index levels from df_idx
levels = df_idx.index.names

# Compute expected by sorting on columns and the setting index
expected = df_none.sort_values(
    by=sort_names, ascending=ascending, axis=0
).set_index(levels)

# Compute result sorting on mix on columns and index levels
result = df_idx.sort_values(by=sort_names, ascending=ascending, axis=0)

tm.assert_frame_equal(result, expected)
