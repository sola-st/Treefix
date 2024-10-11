# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_compression.py
# see gh-15008
compression = compression_only

# We'll complete file extension subsequently.
filename = "test."
filename += _compression_to_extension[compression]

df = pd.DataFrame({"A": [1]})

to_compression = "infer" if to_infer else compression
read_compression = "infer" if read_infer else compression

with tm.ensure_clean(filename) as path:
    df.to_json(path, compression=to_compression)
    result = pd.read_json(path, compression=read_compression)
    tm.assert_frame_equal(result, df)
