# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py

with tm.ensure_clean("__tmp_to_csv_from_csv3__") as path:
    df1 = DataFrame(np.random.randn(3, 1))
    df2 = DataFrame(np.random.randn(3, 1))

    df1.to_csv(path)
    df2.to_csv(path, mode="a", header=False)
    xp = pd.concat([df1, df2])
    rs = read_csv(path, index_col=0)
    rs.columns = [int(label) for label in rs.columns]
    xp.columns = [int(label) for label in xp.columns]
    tm.assert_frame_equal(xp, rs)
