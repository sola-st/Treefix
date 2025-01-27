# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_string.py
df = DataFrame({"\u03c3": np.arange(10.0)})

buf = StringIO()
df.to_string(buf=buf)
buf.getvalue()

buf = StringIO()
df.info(buf=buf)
buf.getvalue()

result = float_frame.to_string()
assert isinstance(result, str)
