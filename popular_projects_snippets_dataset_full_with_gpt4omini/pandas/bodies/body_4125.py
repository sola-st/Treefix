# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# GH#21597 As of 2.0, axis=None reduces over all axes.

df = DataFrame(np.random.randn(4, 4))

result = getattr(df, method)(axis=None)
np_arr = df.to_numpy()
if method in {"skew", "kurt"}:
    comp_mod = pytest.importorskip("scipy.stats")
    if method == "kurt":
        method = "kurtosis"
    expected = getattr(comp_mod, method)(np_arr, bias=False, axis=None)
    tm.assert_almost_equal(result, expected)
else:
    expected = getattr(np, method)(np_arr, axis=None)
    assert result == expected
