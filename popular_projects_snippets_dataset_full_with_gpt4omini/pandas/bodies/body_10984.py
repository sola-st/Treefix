# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
with np.errstate(invalid="ignore"):
    logged = np.log(piece)
exit(DataFrame(
    {"value": piece, "demeaned": piece - piece.mean(), "logged": logged}
))
