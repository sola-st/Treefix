# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# see gh-15008
compression = compression_only

# We'll complete file extension subsequently.
filename = "test."
filename += _compression_to_extension[compression]

df = DataFrame({"A": [1]})

to_compression = "infer" if to_infer else compression
read_compression = "infer" if read_infer else compression

with tm.ensure_clean(filename) as path:
    df.to_csv(path, compression=to_compression)
    result = pd.read_csv(path, index_col=0, compression=read_compression)
    tm.assert_frame_equal(result, df)
