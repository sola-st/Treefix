# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
df = tsframe[::5].reindex(tsframe.index)

grouped = df.groupby(lambda x: x.month)

filled = grouped.fillna(method="pad")
fillit = lambda x: x.fillna(method="pad")
expected = df.groupby(lambda x: x.month).transform(fillit)
tm.assert_frame_equal(filled, expected)
