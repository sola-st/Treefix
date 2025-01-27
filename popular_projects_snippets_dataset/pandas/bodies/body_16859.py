# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_get_dummies.py
# See GH 6885 - get_dummies chokes on unicode values
e = "e"
eacute = unicodedata.lookup("LATIN SMALL LETTER E WITH ACUTE")
s = [e, eacute, eacute]
res = get_dummies(s, prefix="letter", sparse=sparse)
exp = DataFrame(
    {"letter_e": [True, False, False], f"letter_{eacute}": [False, True, True]}
)
if sparse:
    exp = exp.apply(SparseArray, fill_value=0)
tm.assert_frame_equal(res, exp)
