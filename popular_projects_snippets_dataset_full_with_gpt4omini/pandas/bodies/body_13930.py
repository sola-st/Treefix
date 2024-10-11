# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_info.py
io = StringIO()
df = DataFrame(np.random.randn(5, 101))
df.info(buf=io)

io = StringIO()
df.info(buf=io, max_cols=101)
result = io.getvalue()
assert len(result.splitlines()) > 100

expected = result
with option_context("display.max_info_columns", 101):
    io = StringIO()
    df.info(buf=io)
    result = io.getvalue()
    assert result == expected
