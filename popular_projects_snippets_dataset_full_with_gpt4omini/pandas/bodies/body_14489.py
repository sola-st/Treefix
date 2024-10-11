# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_errors.py

with ensure_clean_store(setup_path) as store:

    with catch_warnings(record=True):

        df = tm.makeTimeDataFrame()
        df["string"] = "foo"
        df.loc[df.index[0:4], "string"] = "bar"

        store.put("df", df, format="table")

        # some invalid terms
        msg = re.escape(
            "__init__() missing 1 required positional argument: 'where'"
        )
        with pytest.raises(TypeError, match=msg):
            Term()

        # more invalid
        msg = re.escape(
            "cannot process expression [df.index[3]], "
            "[2000-01-06 00:00:00] is not a valid condition"
        )
        with pytest.raises(ValueError, match=msg):
            store.select("df", "df.index[3]")

        msg = "invalid syntax"
        with pytest.raises(SyntaxError, match=msg):
            store.select("df", "index>")

    # from the docs
path = tmp_path / setup_path
dfq = DataFrame(
    np.random.randn(10, 4),
    columns=list("ABCD"),
    index=date_range("20130101", periods=10),
)
dfq.to_hdf(path, "dfq", format="table", data_columns=True)

# check ok
read_hdf(path, "dfq", where="index>Timestamp('20130104') & columns=['A', 'B']")
read_hdf(path, "dfq", where="A>0 or C>0")

# catch the invalid reference
path = tmp_path / setup_path
dfq = DataFrame(
    np.random.randn(10, 4),
    columns=list("ABCD"),
    index=date_range("20130101", periods=10),
)
dfq.to_hdf(path, "dfq", format="table")

msg = (
    r"The passed where expression: A>0 or C>0\n\s*"
    r"contains an invalid variable reference\n\s*"
    r"all of the variable references must be a reference to\n\s*"
    r"an axis \(e.g. 'index' or 'columns'\), or a data_column\n\s*"
    r"The currently defined references are: index,columns\n"
)
with pytest.raises(ValueError, match=msg):
    read_hdf(path, "dfq", where="A>0 or C>0")
