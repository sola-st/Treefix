# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_sas7bdat.py
df0, test_ix = data_test_ix
for k in test_ix:
    fname = os.path.join(dirpath, f"test{k}.sas7bdat")
    with open(fname, "rb") as f:
        byts = f.read()
    buf = io.BytesIO(byts)
    with pd.read_sas(
        buf, format="sas7bdat", iterator=True, encoding="utf-8"
    ) as rdr:
        df = rdr.read()
    tm.assert_frame_equal(df, df0, check_exact=False)
