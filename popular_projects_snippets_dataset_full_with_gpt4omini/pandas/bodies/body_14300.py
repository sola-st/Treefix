# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_append.py
# GH 11238
df = DataFrame(
    {
        "IX": np.arange(1, 21),
        "Num": np.arange(1, 21),
        "BigNum": np.arange(1, 21) * 88,
        "Str": ["a" for _ in range(20)],
        "LongStr": ["abcde" for _ in range(20)],
    }
)
expected = df.iloc[[0]]

with ensure_clean_store(setup_path) as store:
    store.append_to_multiple(
        {
            "index": ["IX"],
            "nums": ["Num", "BigNum"],
            "strs": ["Str", "LongStr"],
        },
        df.iloc[[0]],
        "index",
        min_itemsize={"Str": 10, "LongStr": 100, "Num": 2},
    )
    result = store.select_as_multiple(["index", "nums", "strs"])
    tm.assert_frame_equal(result, expected)
