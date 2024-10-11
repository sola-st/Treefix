# Extracted from ./data/repos/pandas/pandas/io/xml.py
"""
    Convert extracted raw data.

    This method will return underlying data of extracted XML content.
    The data either has a `read` attribute (e.g. a file object or a
    StringIO/BytesIO) or is a string or bytes that is an XML document.
    """

if isinstance(data, str):
    data = io.StringIO(data)

elif isinstance(data, bytes):
    data = io.BytesIO(data)

exit(data)
