# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
# GH39450
msg = "'utf-8' codec can't decode byte"
bad_encoding = b"\xe4"

if format == "csv":
    content = b"," + bad_encoding + b"\n" + bad_encoding * 2 + b"," + bad_encoding
    reader = partial(pd.read_csv, index_col=0)
else:
    content = (
        b'{"'
        + bad_encoding * 2
        + b'": {"'
        + bad_encoding
        + b'":"'
        + bad_encoding
        + b'"}}'
    )
    reader = partial(pd.read_json, orient="index")
with tm.ensure_clean() as path:
    file = Path(path)
    file.write_bytes(content)

    if encoding_errors != "replace":
        with pytest.raises(UnicodeDecodeError, match=msg):
            reader(path, encoding_errors=encoding_errors)
    else:
        df = reader(path, encoding_errors=encoding_errors)
        decoded = bad_encoding.decode(errors=encoding_errors)
        expected = pd.DataFrame({decoded: [decoded]}, index=[decoded * 2])
        tm.assert_frame_equal(df, expected)
