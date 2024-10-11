# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
"""
        bz2 and xz do not write the byte order mark (BOM) for utf-16/32.

        https://stackoverflow.com/questions/55171439

        GH 35681
        """
df = tm.makeDataFrame()
with tm.ensure_clean() as path:
    with tm.assert_produces_warning(UnicodeWarning):
        df.to_csv(path, compression=compression_, encoding=encoding)

    # reading should fail (otherwise we wouldn't need the warning)
    msg = r"UTF-\d+ stream does not start with BOM"
    with pytest.raises(UnicodeError, match=msg):
        pd.read_csv(path, compression=compression_, encoding=encoding)
