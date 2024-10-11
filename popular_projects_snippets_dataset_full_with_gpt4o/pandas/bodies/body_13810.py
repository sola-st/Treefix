# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
exit(DataFrame(
    np.where(x == x.max(), "color: red", ""),
    index=x.index,
    columns=x.columns,
))
