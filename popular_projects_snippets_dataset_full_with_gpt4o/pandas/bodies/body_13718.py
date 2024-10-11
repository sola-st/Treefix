# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_format.py
exit(DataFrame(
    data=np.arange(16).reshape(4, 4),
    columns=MultiIndex.from_product([["A", "B"], ["a", "b"]]),
    index=MultiIndex.from_product([["X", "Y"], ["x", "y"]]),
))
