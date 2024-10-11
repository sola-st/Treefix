# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
x = np.random.uniform(-100., 100., size=int(1e4)).astype(dtype)
self.assertAllClose(
    self.evaluate(special_math_ops.fresnel_sin(x)),
    self.evaluate(-special_math_ops.fresnel_sin(-x)))
