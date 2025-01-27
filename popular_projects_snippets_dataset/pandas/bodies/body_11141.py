# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py

tsf = tm.makeTimeDataFrame()

grouped = tsf.groupby(lambda x: x.month, group_keys=False)
result = grouped.apply(lambda x: x.sort_values(by="A")[:3])

pieces = [group.sort_values(by="A")[:3] for key, group in grouped]

expected = pd.concat(pieces)
tm.assert_frame_equal(result, expected)

grouped = tsf["A"].groupby(lambda x: x.month, group_keys=False)
result = grouped.apply(lambda x: x.sort_values()[:3])

pieces = [group.sort_values()[:3] for key, group in grouped]

expected = pd.concat(pieces)
tm.assert_series_equal(result, expected)
