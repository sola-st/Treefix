# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
"""
    Assertion helper for checking filepath_or_buffer.
    """

def _assert_filepath_or_buffer_equals(expected):
    if filepath_or_buffer_id == "string":
        with open(filepath_or_buffer, encoding=encoding) as f:
            result = f.read()
    elif filepath_or_buffer_id == "pathlike":
        result = filepath_or_buffer.read_text(encoding=encoding)
    elif filepath_or_buffer_id == "buffer":
        result = filepath_or_buffer.getvalue()
    assert result == expected

exit(_assert_filepath_or_buffer_equals)
