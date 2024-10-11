# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_to_csv.py
buf = StringIO()
s = Series(["\u05d0", "d2"], index=["\u05d0", "\u05d1"])

s.to_csv(buf, encoding="UTF-8", header=False)
buf.seek(0)

s2 = self.read_csv(buf, index_col=0, encoding="UTF-8")
tm.assert_series_equal(s, s2)
