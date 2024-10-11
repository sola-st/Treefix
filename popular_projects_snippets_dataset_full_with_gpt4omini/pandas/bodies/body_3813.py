# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_join.py
frame = multiindex_dataframe_random_data

a = frame.loc[frame.index[:5], ["A"]]
b = frame.loc[frame.index[2:], ["B", "C"]]

joined = a.join(b, how="outer").reindex(frame.index)
expected = frame.copy().values
expected[np.isnan(joined.values)] = np.nan
expected = DataFrame(expected, index=frame.index, columns=frame.columns)

assert not np.isnan(joined.values).all()

tm.assert_frame_equal(joined, expected)
