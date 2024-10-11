# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_select.py
df = DataFrame(
    {
        "a": ["a", "a", "c", "b", "test & test", "c", "b", "e"],
        "b": [1, 2, 3, 4, 5, 6, 7, 8],
    }
)
expected = df[df.a == "test & test"]
with ensure_clean_store(setup_path) as store:
    store.append("test", df, format="table", data_columns=True)
    result = store.select("test", 'a = "test & test"')
tm.assert_frame_equal(expected, result)
