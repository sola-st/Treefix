# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nunique.py
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
