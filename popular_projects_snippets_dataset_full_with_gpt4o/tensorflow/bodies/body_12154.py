# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
r = np.random.RandomState(0)
a = array_ops.placeholder_with_default(r.randn(2, 3), shape=(2, 3))
b = array_ops.placeholder_with_default(r.randn(3, 4), shape=(3, 4))
with self.assertRaises(TypeError):
    _ = special_math_ops.einsum(
        'ij,jk->ik', a, b, name='name', invalid1='value1', invalid2='value2')
