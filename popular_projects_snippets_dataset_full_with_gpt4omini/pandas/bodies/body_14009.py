# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_series_info.py
n = 2500
data = np.array(list("abcdefghij")).take(np.random.randint(0, 10, size=n))
s = Series(data).astype("category")
s.isna()
buf = StringIO()
s.info(buf=buf)

s2 = s[s == "d"]
buf = StringIO()
s2.info(buf=buf)
