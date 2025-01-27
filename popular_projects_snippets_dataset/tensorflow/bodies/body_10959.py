# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
for shape in [(10, 10), None]:
    with self.cached_session():
        x = array_ops.placeholder(dtypes.float32, shape)
        # Expect a ValueError because the dimensions are wrong
        with self.assertRaises(ValueError):
            gradients.hessians(x, x)
