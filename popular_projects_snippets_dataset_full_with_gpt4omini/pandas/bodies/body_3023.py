# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
# GH#14353

# Get levels from df_idx
levels = df_idx.index.names

# Compute expected by sorting on axis=0, setting index levels, and then
# transposing. For some cases this will result in a frame with
# multiple column levels
expected = (
    df_none.sort_values(by=sort_names, ascending=ascending, axis=0)
    .set_index(levels)
    .T
)

# Compute result by transposing and sorting on axis=1.
result = df_idx.T.sort_values(by=sort_names, ascending=ascending, axis=1)

tm.assert_frame_equal(result, expected)
