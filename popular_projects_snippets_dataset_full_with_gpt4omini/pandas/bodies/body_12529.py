# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
base_path = os.path.basename(html_encoding_file)
root = os.path.splitext(base_path)[0]
_, encoding = root.split("_")

try:
    with open(html_encoding_file, "rb") as fobj:
        from_string = self.read_html(
            fobj.read(), encoding=encoding, index_col=0
        ).pop()

    with open(html_encoding_file, "rb") as fobj:
        from_file_like = self.read_html(
            BytesIO(fobj.read()), encoding=encoding, index_col=0
        ).pop()

    from_filename = self.read_html(
        html_encoding_file, encoding=encoding, index_col=0
    ).pop()
    tm.assert_frame_equal(from_string, from_file_like)
    tm.assert_frame_equal(from_string, from_filename)
except Exception:
    # seems utf-16/32 fail on windows
    if is_platform_windows():
        if "16" in encoding or "32" in encoding:
            pytest.skip()
    raise
