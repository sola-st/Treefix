# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_sas7bdat.py
# Support of different SAS date/datetime formats (PR #15871)
fname = datapath("io", "sas", "data", "datetime.sas7bdat")
df = pd.read_sas(fname)
fname = datapath("io", "sas", "data", "datetime.csv")
df0 = pd.read_csv(
    fname, parse_dates=["Date1", "Date2", "DateTime", "DateTimeHi", "Taiw"]
)
# GH 19732: Timestamps imported from sas will incur floating point errors
df[df.columns[3]] = df.iloc[:, 3].dt.round("us")
tm.assert_frame_equal(df, df0)
