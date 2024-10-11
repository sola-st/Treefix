# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
file_name = f"test.{file_ext}"
archive_name = "test.dta"
df = DataFrame(np.random.randn(10, 2), columns=list("AB"))
df.index.name = "index"
with tm.ensure_clean(file_name) as path:
    compression = {"method": method, "archive_name": archive_name}
    df.to_stata(path, compression=compression)
    if method == "zip" or file_ext == "zip":
        with zipfile.ZipFile(path, "r") as zp:
            assert len(zp.filelist) == 1
            assert zp.filelist[0].filename == archive_name
            fp = io.BytesIO(zp.read(zp.filelist[0]))
    else:
        fp = path
    reread = read_stata(fp, index_col="index")

expected = df.copy()
expected.index = expected.index.astype(np.int32)
tm.assert_frame_equal(reread, expected)
