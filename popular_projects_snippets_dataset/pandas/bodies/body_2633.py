# Extracted from ./data/repos/pandas/pandas/tests/frame/test_subclass.py
# GH 13977
df = tm.SubclassedDataFrame({"a": [1]})
for i, row in df.iterrows():
    assert isinstance(row, tm.SubclassedSeries)
    tm.assert_series_equal(row, df.loc[i])
