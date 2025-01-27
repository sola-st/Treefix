# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py

df = tm.makeCustomDataframe(5, 2)
# vertical empty
tm.assert_frame_equal(
    df.iloc[:, []],
    df.iloc[:, :0],
    check_index_type=True,
    check_column_type=True,
)
# horizontal empty
tm.assert_frame_equal(
    df.iloc[[], :],
    df.iloc[:0, :],
    check_index_type=True,
    check_column_type=True,
)
# horizontal empty
tm.assert_frame_equal(
    df.iloc[[]], df.iloc[:0, :], check_index_type=True, check_column_type=True
)
