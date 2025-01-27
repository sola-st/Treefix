# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
df = DataFrame([data])
if method in ["to_latex"]:  # uses styler implementation
    pytest.importorskip("jinja2")

if filepath_or_buffer_id not in ["string", "pathlike"] and encoding is not None:
    with pytest.raises(
        ValueError, match="buf is not a file name and encoding is specified."
    ):
        getattr(df, method)(buf=filepath_or_buffer, encoding=encoding)
elif encoding == "foo":
    with pytest.raises(LookupError, match="unknown encoding"):
        getattr(df, method)(buf=filepath_or_buffer, encoding=encoding)
else:
    expected = getattr(df, method)()
    getattr(df, method)(buf=filepath_or_buffer, encoding=encoding)
    assert_filepath_or_buffer_equals(expected)
