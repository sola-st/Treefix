# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
s = Series([1, 2], name="\u05e2\u05d1\u05e8\u05d9\u05ea")
sf = fmt.SeriesFormatter(s, name="\u05e2\u05d1\u05e8\u05d9\u05ea")
sf._get_footer()  # should not raise exception
