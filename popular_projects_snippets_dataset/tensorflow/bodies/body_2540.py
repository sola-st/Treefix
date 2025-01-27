# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
assert expected is not None
results = self._Execute(c, arguments)
self.assertLen(results, len(expected))
for result, e in zip(results, expected):
    # Numpy's comparison methods are a bit too lenient by treating inputs as
    # "array-like", meaning that scalar 4 will be happily compared equal to
    # [[4]]. We'd like to be more strict so assert shapes as well.
    self.assertEqual(np.asanyarray(result).shape, np.asanyarray(e).shape)
    assert_func(result, e)
