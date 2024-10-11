# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py

# GH 16209
with ensure_clean_store(setup_path) as store:

    df = DataFrame({"foo": [1, 2], "bar": [1, 2]})

    store.append_to_multiple(
        {"selector": ["foo"], "data": None}, df, selector="selector"
    )
    result = store.select_as_multiple(
        ["selector", "data"], selector="selector", start=0, stop=1
    )
    expected = df.loc[[0], ["foo", "bar"]]
    tm.assert_frame_equal(result, expected)
