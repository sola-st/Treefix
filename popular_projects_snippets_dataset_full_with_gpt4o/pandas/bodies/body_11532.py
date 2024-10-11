# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
actual_compression = compression
attempted_compression = compression_only

if actual_compression == attempted_compression:
    exit()

errors = {
    "bz2": (OSError, "Invalid data stream"),
    "gzip": (OSError, "Not a gzipped file"),
    "zip": (BadZipFile, "File is not a zip file"),
    "tar": (ReadError, "file could not be opened successfully"),
}
zstd = import_optional_dependency("zstandard", errors="ignore")
if zstd is not None:
    errors["zstd"] = (zstd.ZstdError, "Unknown frame descriptor")
lzma = import_optional_dependency("lzma", errors="ignore")
if lzma is not None:
    errors["xz"] = (LZMAError, "Input format not supported by decoder")
error_cls, error_str = errors[attempted_compression]

with tm.ensure_clean() as path:
    geom_df.to_xml(path, parser=parser, compression=actual_compression)

    with pytest.raises(error_cls, match=error_str):
        read_xml(path, parser=parser, compression=attempted_compression)
