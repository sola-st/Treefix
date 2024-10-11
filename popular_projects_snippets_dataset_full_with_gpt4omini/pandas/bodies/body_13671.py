# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_highlight.py
# GH 45804
exit(DataFrame(
    {"A": [0, np.nan, 10], "B": [1, request.param[0], 2]}, dtype=request.param[1]
))
