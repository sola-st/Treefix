# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop_duplicates.py
# GH#14192
df = DataFrame(
    {
        "a": [1, 1, 1, "one", "one"],
        "b": [2, 2, np.nan, np.nan, np.nan],
        "c": [3, 3, np.nan, np.nan, "three"],
        "d": [1, 2, 3, 4, 4],
        "e": [
            datetime(2015, 1, 1),
            datetime(2015, 1, 1),
            datetime(2015, 2, 1),
            NaT,
            NaT,
        ],
    }
)
for column in df.columns:
    dropped_frame = df[[column]].drop_duplicates(keep=keep)
    dropped_series = df[column].drop_duplicates(keep=keep)
    tm.assert_frame_equal(dropped_frame, dropped_series.to_frame())
