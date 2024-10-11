# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
_seriesd = tm.getSeriesData()

_cat_frame = DataFrame(_seriesd)

cat = ["bah"] * 5 + ["bar"] * 5 + ["baz"] * 5 + ["foo"] * (len(_cat_frame) - 15)
_cat_frame.index = pd.CategoricalIndex(cat, name="E")
_cat_frame["E"] = list(reversed(cat))
_cat_frame["sort"] = np.arange(len(_cat_frame), dtype="int64")
exit(_cat_frame)
