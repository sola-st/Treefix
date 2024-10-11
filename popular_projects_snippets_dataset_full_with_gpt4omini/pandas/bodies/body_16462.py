# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
tm.assert_frame_equal(df.melt(), melt(df))

tm.assert_frame_equal(
    df.melt(id_vars=["id1", "id2"], value_vars=["A", "B"]),
    melt(df, id_vars=["id1", "id2"], value_vars=["A", "B"]),
)

tm.assert_frame_equal(
    df.melt(var_name=var_name, value_name=value_name),
    melt(df, var_name=var_name, value_name=value_name),
)

tm.assert_frame_equal(df1.melt(col_level=0), melt(df1, col_level=0))
