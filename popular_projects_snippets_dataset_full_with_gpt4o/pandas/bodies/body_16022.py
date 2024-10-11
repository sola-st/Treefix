# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_cov_corr.py
from scipy import stats

# kendall and spearman
A = tm.makeTimeSeries()
B = tm.makeTimeSeries()
A[-5:] = A[:5]
result = A.corr(B, method="kendall")
expected = stats.kendalltau(A, B)[0]
tm.assert_almost_equal(result, expected)

result = A.corr(B, method="spearman")
expected = stats.spearmanr(A, B)[0]
tm.assert_almost_equal(result, expected)

# results from R
A = Series(
    [
        -0.89926396,
        0.94209606,
        -1.03289164,
        -0.95445587,
        0.76910310,
        -0.06430576,
        -2.09704447,
        0.40660407,
        -0.89926396,
        0.94209606,
    ]
)
B = Series(
    [
        -1.01270225,
        -0.62210117,
        -1.56895827,
        0.59592943,
        -0.01680292,
        1.17258718,
        -1.06009347,
        -0.10222060,
        -0.89076239,
        0.89372375,
    ]
)
kexp = 0.4319297
sexp = 0.5853767
tm.assert_almost_equal(A.corr(B, method="kendall"), kexp)
tm.assert_almost_equal(A.corr(B, method="spearman"), sexp)
