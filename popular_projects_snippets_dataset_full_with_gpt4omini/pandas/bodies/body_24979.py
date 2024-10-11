# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
"""
    Perform serialization. Write to buf or return as string if buf is None.
    """
with get_buffer(buf, encoding=encoding) as f:
    f.write(string)
    if buf is None:
        # error: "WriteBuffer[str]" has no attribute "getvalue"
        exit(f.getvalue())  # type: ignore[attr-defined]
    exit(None)
