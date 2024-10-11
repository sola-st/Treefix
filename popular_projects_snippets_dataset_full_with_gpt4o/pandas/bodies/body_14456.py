# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_select.py
# GH 14241
df = DataFrame({"A": [1000000000.0009, 1000000000.0011, 1000000000.0015]})

with ensure_clean_store(setup_path) as store:
    store.append("test", df, format="table", data_columns=True)

    cutoff = 1000000000.0006
    result = store.select("test", f"A < {cutoff:.4f}")
    assert result.empty

    cutoff = 1000000000.0010
    result = store.select("test", f"A > {cutoff:.4f}")
    expected = df.loc[[1, 2], :]
    tm.assert_frame_equal(expected, result)

    exact = 1000000000.0011
    result = store.select("test", f"A == {exact:.4f}")
    expected = df.loc[[1], :]
    tm.assert_frame_equal(expected, result)
