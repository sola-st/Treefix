# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
exit(DataFrame(
    {
        "outer": ["a", "a", "a", "b", "b", "b"],
        "inner": [1, 2, 2, 2, 1, 1],
        "A": np.arange(6, 0, -1),
        ("B", 5): ["one", "one", "two", "two", "one", "one"],
    }
))
