# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py
# GH9057

types_should_fail = [
    tm.makeIntIndex,
    tm.makeFloatIndex,
    tm.makeDateIndex,
    tm.makeTimedeltaIndex,
    tm.makePeriodIndex,
]
types_should_run = [
    tm.makeStringIndex,
    tm.makeCategoricalIndex,
]

for index in types_should_fail:
    df = DataFrame(np.random.randn(10, 2), columns=index(2))
    path = tmp_path / setup_path
    with catch_warnings(record=True):
        msg = "cannot have non-object label DataIndexableCol"
        with pytest.raises(ValueError, match=msg):
            df.to_hdf(path, "df", format="table", data_columns=True)

for index in types_should_run:
    df = DataFrame(np.random.randn(10, 2), columns=index(2))
    path = tmp_path / setup_path
    with catch_warnings(record=True):
        df.to_hdf(path, "df", format="table", data_columns=True)
        result = read_hdf(path, "df", where=f"index = [{df.index[0]}]")
        assert len(result)
