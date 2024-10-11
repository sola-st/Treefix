# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
base = get_random_path
path1 = base + compression_ext
path2 = base + ".raw"
compression = self._extension_to_compression.get(compression_ext.lower())

with tm.ensure_clean(path1) as p1, tm.ensure_clean(path2) as p2:
    df = tm.makeDataFrame()

    # write to compressed file by inferred compression method
    df.to_pickle(p1)

    # decompress
    with tm.decompress_file(p1, compression=compression) as f:
        with open(p2, "wb") as fh:
            fh.write(f.read())

            # read decompressed file
    df2 = pd.read_pickle(p2, compression=None)

    tm.assert_frame_equal(df, df2)
