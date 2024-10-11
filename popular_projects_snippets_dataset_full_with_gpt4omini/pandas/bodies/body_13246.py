# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_sas7bdat.py
# GH 31243
fname = datapath("io", "sas", "data", "0x40controlbyte.sas7bdat")
df = pd.read_sas(fname, encoding="ascii")
fname = datapath("io", "sas", "data", "0x40controlbyte.csv")
df0 = pd.read_csv(fname, dtype="object")
tm.assert_frame_equal(df, df0)
