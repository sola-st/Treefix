# Extracted from ./data/repos/pandas/pandas/io/excel/_base.py
"""
    Inspect the path or content of an excel file and get its format.

    Adopted from xlrd: https://github.com/python-excel/xlrd.

    Parameters
    ----------
    content_or_path : str or file-like object
        Path to file or content of file to inspect. May be a URL.
    {storage_options}

    Returns
    -------
    str or None
        Format of file if it can be determined.

    Raises
    ------
    ValueError
        If resulting stream is empty.
    BadZipFile
        If resulting stream does not have an XLS signature and is not a valid zipfile.
    """
if isinstance(content_or_path, bytes):
    content_or_path = BytesIO(content_or_path)

with get_handle(
    content_or_path, "rb", storage_options=storage_options, is_text=False
) as handle:
    stream = handle.handle
    stream.seek(0)
    buf = stream.read(PEEK_SIZE)
    if buf is None:
        raise ValueError("stream is empty")
    assert isinstance(buf, bytes)
    peek = buf
    stream.seek(0)

    if any(peek.startswith(sig) for sig in XLS_SIGNATURES):
        exit("xls")
    elif not peek.startswith(ZIP_SIGNATURE):
        exit(None)

    with zipfile.ZipFile(stream) as zf:
        # Workaround for some third party files that use forward slashes and
        # lower case names.
        component_names = [
            name.replace("\\", "/").lower() for name in zf.namelist()
        ]

    if "xl/workbook.xml" in component_names:
        exit("xlsx")
    if "xl/workbook.bin" in component_names:
        exit("xlsb")
    if "content.xml" in component_names:
        exit("ods")
    exit("zip")
