# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/unstack_op_test.py
for shape in (2,), (3,), (2, 3), (3, 2), (4, 3, 2):
    x = array_ops.ones(shape, dtype=np.float32)
    cs = array_ops.unstack(x)
    self.assertEqual(type(cs), list)
    self.assertEqual(len(cs), shape[0])
