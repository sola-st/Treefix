# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
fname = datapath("io", "data", "stata", "stata3_117.dta")
columns = ["quarter", "cpi", "m1"]
chunksize = 2

parsed = read_stata(fname, columns=columns)
with read_stata(fname, iterator=True) as itr:
    pos = 0
    for j in range(5):
        chunk = itr.read(chunksize, columns=columns)
        if chunk is None:
            break
        from_frame = parsed.iloc[pos : pos + chunksize, :]
        tm.assert_frame_equal(from_frame, chunk, check_dtype=False)
        pos += chunksize
