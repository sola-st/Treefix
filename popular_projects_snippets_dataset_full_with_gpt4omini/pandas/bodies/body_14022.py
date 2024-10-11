# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
if filepath_or_buffer_id == "string":
    with open(filepath_or_buffer, encoding=encoding) as f:
        result = f.read()
elif filepath_or_buffer_id == "pathlike":
    result = filepath_or_buffer.read_text(encoding=encoding)
elif filepath_or_buffer_id == "buffer":
    result = filepath_or_buffer.getvalue()
assert result == expected
