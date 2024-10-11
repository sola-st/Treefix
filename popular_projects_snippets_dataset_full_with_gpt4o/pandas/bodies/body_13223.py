# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_sas7bdat.py
df0, test_ix = data_test_ix
for k in test_ix:
    fname = os.path.join(dirpath, f"test{k}.sas7bdat")
    with pd.read_sas(fname, iterator=True, encoding="utf-8") as rdr:
        df = rdr.read(2)
        tm.assert_frame_equal(df, df0.iloc[0:2, :])
        df = rdr.read(3)
        tm.assert_frame_equal(df, df0.iloc[2:5, :])
