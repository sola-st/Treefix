# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_spec_test.py
assert isinstance(x, dict) and isinstance(y, dict)
self.assertEqual(set(x), set(y))
for key in x:
    self.assertAllEqual(x[key], y[key])
