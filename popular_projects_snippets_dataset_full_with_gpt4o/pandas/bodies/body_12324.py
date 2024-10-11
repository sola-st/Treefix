# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
fname = datapath("io", "data", "stata", "stata3_117.dta")

parsed = read_stata(fname)

with read_stata(fname, iterator=True) as itr:
    chunk = itr.read(5)
    tm.assert_frame_equal(parsed.iloc[0:5, :], chunk)

with read_stata(fname, chunksize=5) as itr:
    chunk = list(itr)
    tm.assert_frame_equal(parsed.iloc[0:5, :], chunk[0])

with read_stata(fname, iterator=True) as itr:
    chunk = itr.get_chunk(5)
    tm.assert_frame_equal(parsed.iloc[0:5, :], chunk)

with read_stata(fname, chunksize=5) as itr:
    chunk = itr.get_chunk()
    tm.assert_frame_equal(parsed.iloc[0:5, :], chunk)

# GH12153
with read_stata(fname, chunksize=4) as itr:
    from_chunks = pd.concat(itr)
tm.assert_frame_equal(parsed, from_chunks)
