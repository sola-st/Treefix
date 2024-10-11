# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_sas7bdat.py
fname = datapath("io", "sas", "data", "test_12659.sas7bdat")
df = pd.read_sas(fname)
fname = datapath("io", "sas", "data", "test_12659.csv")
df0 = pd.read_csv(fname)
df0 = df0.astype(np.float64)
tm.assert_frame_equal(df, df0)
