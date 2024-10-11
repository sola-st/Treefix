# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_nlargest.py
exit(pd.DataFrame(
    {
        "a": np.random.permutation(10),
        "b": list(ascii_lowercase[:10]),
        "c": np.random.permutation(10).astype("float64"),
    }
))
