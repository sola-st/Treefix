# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_html.py
midx = MultiIndex.from_product([["a", "b"], ["c", "d"]])
exit(Styler(DataFrame(np.arange(16).reshape(4, 4), index=midx, columns=midx)))
