# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
exit(DataFrame(
    {
        "key1": get_test_data(n=10),
        "key2": get_test_data(ngroups=4, n=10),
        "value": np.random.randn(10),
    }
))
