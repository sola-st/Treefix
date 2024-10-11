# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
# In addition to Tensors, we also support raw numpy arrays as inputs.
r = np.random.RandomState(0)
s = 'ijk,ijl,ikl->i'
x = r.randn(1, 2, 3)
y = r.randn(1, 2, 4)
z = r.randn(1, 3, 4)

a = np.einsum(s, x, y, z)
b = self.evaluate(special_math_ops.einsum(s, x, y, z))
self.assertAllClose(a, b, atol=1e-4, rtol=1e-4)
