# Extracted from ./data/repos/pandas/pandas/tests/extension/base/printing.py
buf = io.StringIO()
pd.DataFrame({"A": data}).info(buf=buf)
result = buf.getvalue()
assert data.dtype.name in result
