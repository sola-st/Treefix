# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_read_fwf.py
data = """
AA   BBB  C
12   345  6
78   901  2
""".strip()

msg = "No rows from which to infer column width"
with pytest.raises(EmptyDataError, match=msg):
    read_fwf(StringIO(data), skiprows=3)
