# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
# Issue #8621
df = DataFrame(np.random.randn(1, 100010), columns=None, index=None)
with tm.ensure_clean() as filename:
    df.to_csv(filename, header=False, index=False)
    rs = read_csv(filename, header=None)
    tm.assert_frame_equal(rs, df)
