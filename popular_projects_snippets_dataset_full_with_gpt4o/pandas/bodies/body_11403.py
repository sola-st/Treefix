# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
base = get_random_path
path1 = base + ".compressed"
path2 = base + ".raw"

with tm.ensure_clean(path1) as p1, tm.ensure_clean(path2) as p2:
    df = tm.makeDataFrame()

    # write to compressed file
    df.to_pickle(p1, compression=compression)

    # decompress
    with tm.decompress_file(p1, compression=compression) as f:
        with open(p2, "wb") as fh:
            fh.write(f.read())

            # read decompressed file
    df2 = pd.read_pickle(p2, compression=None)

    tm.assert_frame_equal(df, df2)
