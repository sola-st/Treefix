# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_series_info.py
buf = StringIO()
series.info(buf=buf)
if plus:
    assert "+" in buf.getvalue()
else:
    assert "+" not in buf.getvalue()
