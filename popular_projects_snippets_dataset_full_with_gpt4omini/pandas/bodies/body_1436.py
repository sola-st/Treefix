# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
start_dataframe = DataFrame(
    {
        "a": [1, 2, 3],
        "b": [1.0, 2.0, 3.0],
        "c": [datetime(2000, 1, 1), datetime(2000, 1, 2), datetime(2000, 1, 3)],
        "d": ["a", "b", "c"],
    }
)
start_dataframe.iloc[0] = None

exp = DataFrame(
    {
        "a": [np.nan, 2, 3],
        "b": [np.nan, 2.0, 3.0],
        "c": [NaT, datetime(2000, 1, 2), datetime(2000, 1, 3)],
        "d": [None, "b", "c"],
    }
)
tm.assert_frame_equal(start_dataframe, exp)
