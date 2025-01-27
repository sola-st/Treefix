# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_info.py
buf = StringIO()
df = DataFrame(1, columns=list("ab"), index=[1, 2, 3])
df.info(buf=buf)
assert "+" not in buf.getvalue()

buf = StringIO()
df = DataFrame(1, columns=list("ab"), index=list("ABC"))
df.info(buf=buf)
assert "+" in buf.getvalue()

buf = StringIO()
df = DataFrame(
    1, columns=list("ab"), index=MultiIndex.from_product([range(3), range(3)])
)
df.info(buf=buf)
assert "+" not in buf.getvalue()

buf = StringIO()
df = DataFrame(
    1, columns=list("ab"), index=MultiIndex.from_product([range(3), ["foo", "bar"]])
)
df.info(buf=buf)
assert "+" in buf.getvalue()
