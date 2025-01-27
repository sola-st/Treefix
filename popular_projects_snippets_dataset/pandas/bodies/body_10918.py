# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nunique.py
def check_nunique(df, keys, as_index=True):
    original_df = df.copy()
    gr = df.groupby(keys, as_index=as_index, sort=sort)
    left = gr["julie"].nunique(dropna=dropna)

    gr = df.groupby(keys, as_index=as_index, sort=sort)
    right = gr["julie"].apply(Series.nunique, dropna=dropna)
    if not as_index:
        right = right.reset_index(drop=True)

    if as_index:
        tm.assert_series_equal(left, right, check_names=False)
    else:
        tm.assert_frame_equal(left, right, check_names=False)
    tm.assert_frame_equal(df, original_df)

days = date_range("2015-08-23", periods=10)

frame = DataFrame(
    {
        "jim": np.random.choice(list(ascii_lowercase), n),
        "joe": np.random.choice(days, n),
        "julie": np.random.randint(0, m, n),
    }
)

check_nunique(frame, ["jim"])
check_nunique(frame, ["jim", "joe"])

frame.loc[1::17, "jim"] = None
frame.loc[3::37, "joe"] = None
frame.loc[7::19, "julie"] = None
frame.loc[8::19, "julie"] = None
frame.loc[9::19, "julie"] = None

check_nunique(frame, ["jim"])
check_nunique(frame, ["jim", "joe"])
check_nunique(frame, ["jim"], as_index=False)
check_nunique(frame, ["jim", "joe"], as_index=False)
