# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_info.py
frame = DataFrame(np.random.randn(5, num_columns))
with option_context("display.max_info_columns", max_info_columns):
    io_default = StringIO()
    frame.info(buf=io_default)
    result = io_default.getvalue()

    io_explicit = StringIO()
    frame.info(buf=io_explicit, verbose=verbose)
    expected = io_explicit.getvalue()

    assert result == expected
