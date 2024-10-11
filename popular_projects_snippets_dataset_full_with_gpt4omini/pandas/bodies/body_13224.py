# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_sas7bdat.py
df0, test_ix = data_test_ix
for k in test_ix:
    fname = Path(os.path.join(dirpath, f"test{k}.sas7bdat"))
    df = pd.read_sas(fname, encoding="utf-8")
    tm.assert_frame_equal(df, df0)
