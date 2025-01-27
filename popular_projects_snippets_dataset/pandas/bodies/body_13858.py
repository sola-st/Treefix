# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_non_unique.py
exit(DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    index=["i", "j", "j"],
    columns=["c", "d", "d"],
    dtype=float,
))
