# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py
# GH 17021
df = DataFrame(
    {
        "a": Series([20111010, 20111011, 20111012]),
        "b": Series(["ab", "cd", "ab"]),
    }
)

with ensure_clean_store(setup_path) as store:
    store.append("test_dataset", df)

    result = store.select("test_dataset", start=start, stop=stop)
    tm.assert_frame_equal(df[start:stop], result)
