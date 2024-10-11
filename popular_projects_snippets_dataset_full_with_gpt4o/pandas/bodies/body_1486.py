# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
exit(DataFrame(
    {
        "date": date_range("2000-01-01", "2000-01-5"),
        "val": Series(range(5), dtype=np.int64),
    }
))
