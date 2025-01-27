# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_select.py

pp = tmp_path / "params.hdf"
hh = tmp_path / "hist.hdf"

# use non-trivial selection criteria
params = DataFrame({"A": [1, 1, 2, 2, 3]})
params.to_hdf(pp, "df", mode="w", format="table", data_columns=["A"])

selection = read_hdf(pp, "df", where="A=[2,3]")
hist = DataFrame(
    np.random.randn(25, 1),
    columns=["data"],
    index=MultiIndex.from_tuples(
        [(i, j) for i in range(5) for j in range(5)], names=["l1", "l2"]
    ),
)

hist.to_hdf(hh, "df", mode="w", format="table")

expected = read_hdf(hh, "df", where="l1=[2, 3, 4]")

# scope with list like
l0 = selection.index.tolist()  # noqa:F841
with HDFStore(hh) as store:
    result = store.select("df", where="l1=l0")
    tm.assert_frame_equal(result, expected)

result = read_hdf(hh, "df", where="l1=l0")
tm.assert_frame_equal(result, expected)

# index
index = selection.index  # noqa:F841
result = read_hdf(hh, "df", where="l1=index")
tm.assert_frame_equal(result, expected)

result = read_hdf(hh, "df", where="l1=selection.index")
tm.assert_frame_equal(result, expected)

result = read_hdf(hh, "df", where="l1=selection.index.tolist()")
tm.assert_frame_equal(result, expected)

result = read_hdf(hh, "df", where="l1=list(selection.index)")
tm.assert_frame_equal(result, expected)

# scope with index
with HDFStore(hh) as store:
    result = store.select("df", where="l1=index")
    tm.assert_frame_equal(result, expected)

    result = store.select("df", where="l1=selection.index")
    tm.assert_frame_equal(result, expected)

    result = store.select("df", where="l1=selection.index.tolist()")
    tm.assert_frame_equal(result, expected)

    result = store.select("df", where="l1=list(selection.index)")
    tm.assert_frame_equal(result, expected)
