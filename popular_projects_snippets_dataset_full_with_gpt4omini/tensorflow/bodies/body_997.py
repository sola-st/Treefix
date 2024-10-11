# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
features = np.array(features, dtype=dtype)
zero = np.asarray(0).astype(dtype)
expected = np.logaddexp(zero, features).astype(dtype)
self._assertOpOutputMatchesExpected(
    nn_ops.softplus,
    features,
    expected=expected,
    equality_test=equality_test,
    rtol=rtol,
    atol=atol)
