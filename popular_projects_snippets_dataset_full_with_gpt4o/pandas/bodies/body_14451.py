# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_select.py

# can't use more than one filter (atm)

df = tm.makeTimeDataFrame()

with ensure_clean_store(setup_path) as store:
    store.put("df", df, format="table")

    msg = "unable to collapse Joint Filters"
    # not implemented
    with pytest.raises(NotImplementedError, match=msg):
        store.select("df", "columns=['A'] | columns=['B']")

    # in theory we could deal with this
    with pytest.raises(NotImplementedError, match=msg):
        store.select("df", "columns=['A','B'] & columns=['C']")
