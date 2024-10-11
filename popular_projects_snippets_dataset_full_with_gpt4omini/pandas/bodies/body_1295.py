# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_categorical.py
exit(DataFrame(
    {
        "A": np.arange(6, dtype="int64"),
    },
    index=CategoricalIndex(list("aabbca"), dtype=CDT(list("cabe")), name="B"),
))
