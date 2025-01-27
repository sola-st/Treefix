# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py

aa = DataFrame({"A": range(100000)})
aa["B"] = aa.A + 1.0
aa["C"] = aa.A + 2.0
aa["D"] = aa.A + 3.0

with tm.ensure_clean() as filename:
    aa.to_csv(filename, chunksize=chunksize)
    rs = read_csv(filename, index_col=0)
    tm.assert_frame_equal(rs, aa)
