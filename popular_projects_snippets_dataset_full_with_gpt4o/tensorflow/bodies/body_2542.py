# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
self._ExecuteAndAssertWith(
    functools.partial(np.testing.assert_allclose, rtol=rtol, atol=atol),
    c, arguments, expected)
