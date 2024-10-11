# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

x = api.converted_call(np.arange, (5,), None, options=DEFAULT_RECURSIVE)

self.assertAllEqual(x, list(range(5)))
