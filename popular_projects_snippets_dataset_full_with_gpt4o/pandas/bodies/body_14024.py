# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
r = repr(df)
c1 = r.split("\n")[0].startswith("<class")
c2 = r.split("\n")[0].startswith(r"&lt;class")  # _repr_html_
exit(c1 or c2)
