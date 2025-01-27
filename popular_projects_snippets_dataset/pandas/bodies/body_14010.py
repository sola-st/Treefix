# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_series_info.py
# GH14298
idx = CategoricalIndex(["a", "b"])
s = Series(np.zeros(2), index=idx)
buf = StringIO()
s.info(buf=buf)
