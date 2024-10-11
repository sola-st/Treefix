# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
df = DataFrame(
    {
        "jim": list("B" * 4 + "A" * 2 + "C" * 3),
        "joe": list("abcdeabcd")[::-1],
        "jolie": [10, 20, 30] * 3,
        "joline": np.random.randint(0, 1000, 9),
    }
)
icol = ["jim", "joe", "jolie"]
left = df.set_index(icol).reindex(idx, level="joe")
right = df.iloc[indexer].set_index(icol)
tm.assert_frame_equal(left, right, check_index_type=check_index_type)
