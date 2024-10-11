# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
base = get_random_path
path1 = base + ".raw"
path2 = base + ".compressed"

with tm.ensure_clean(path1) as p1, tm.ensure_clean(path2) as p2:
    df = tm.makeDataFrame()

    # write to uncompressed file
    df.to_pickle(p1, compression=None)

    # compress
    self.compress_file(p1, p2, compression=compression)

    # read compressed file
    df2 = pd.read_pickle(p2, compression=compression)
    tm.assert_frame_equal(df, df2)
