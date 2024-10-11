# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# GH 26023
method = compression_only
df = DataFrame({"ABC": [1]})
filename = "to_csv_compress_as_dict."
extension = {
    "gzip": "gz",
    "zstd": "zst",
}.get(method, method)
filename += extension
with tm.ensure_clean(filename) as path:
    df.to_csv(path, compression={"method": method})
    read_df = pd.read_csv(path, index_col=0)
    tm.assert_frame_equal(read_df, df)
