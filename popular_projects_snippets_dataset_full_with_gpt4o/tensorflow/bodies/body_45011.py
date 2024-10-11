# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py
x = api.converted_call(np.power, (2, 2), None, options=DEFAULT_RECURSIVE)
self.assertAllEqual(x, 4)
