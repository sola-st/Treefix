# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_sas7bdat.py
fname = datapath("io", "sas", "data", "dates_null.sas7bdat")
df = pd.read_sas(fname, encoding="utf-8")

expected = pd.DataFrame(
    {
        "datecol": [
            datetime(9999, 12, 29),
            pd.NaT,
        ],
        "datetimecol": [
            datetime(9999, 12, 29, 23, 59, 59, 998993),
            pd.NaT,
        ],
    },
)
tm.assert_frame_equal(df, expected)
