# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
file_name = "dta_inferred_compression.dta"
if compression:
    if use_dict:
        file_ext = compression
    else:
        file_ext = _compression_to_extension[compression]
    file_name += f".{file_ext}"
compression_arg = compression
if infer:
    compression_arg = "infer"
if use_dict:
    compression_arg = {"method": compression}

df = DataFrame(np.random.randn(10, 2), columns=list("AB"))
df.index.name = "index"
with tm.ensure_clean(file_name) as path:
    df.to_stata(path, version=version, compression=compression_arg)
    if compression == "gzip":
        with gzip.open(path, "rb") as comp:
            fp = io.BytesIO(comp.read())
    elif compression == "zip":
        with zipfile.ZipFile(path, "r") as comp:
            fp = io.BytesIO(comp.read(comp.filelist[0]))
    elif compression == "tar":
        with tarfile.open(path) as tar:
            fp = io.BytesIO(tar.extractfile(tar.getnames()[0]).read())
    elif compression == "bz2":
        with bz2.open(path, "rb") as comp:
            fp = io.BytesIO(comp.read())
    elif compression == "zstd":
        zstd = pytest.importorskip("zstandard")
        with zstd.open(path, "rb") as comp:
            fp = io.BytesIO(comp.read())
    elif compression == "xz":
        lzma = pytest.importorskip("lzma")
        with lzma.open(path, "rb") as comp:
            fp = io.BytesIO(comp.read())
    elif compression is None:
        fp = path
    reread = read_stata(fp, index_col="index")

expected = df.copy()
expected.index = expected.index.astype(np.int32)
tm.assert_frame_equal(reread, expected)
