# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_boxplot_method.py
# API change in https://github.com/pandas-dev/pandas/pull/7096

df = DataFrame(
    np.random.randn(6, 4),
    index=list(string.ascii_letters[:6]),
    columns=["one", "two", "three", "four"],
)
msg = "return_type must be {'axes', 'dict', 'both'}"
with pytest.raises(ValueError, match=msg):
    df.boxplot(return_type="NOT_A_TYPE")

result = df.boxplot()
self._check_box_return_type(result, "axes")

with tm.assert_produces_warning(False):
    result = df.boxplot(return_type="dict")
self._check_box_return_type(result, "dict")

with tm.assert_produces_warning(False):
    result = df.boxplot(return_type="axes")
self._check_box_return_type(result, "axes")

with tm.assert_produces_warning(False):
    result = df.boxplot(return_type="both")
self._check_box_return_type(result, "both")
