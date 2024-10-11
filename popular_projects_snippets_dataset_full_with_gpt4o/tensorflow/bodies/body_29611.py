# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/unstack_op_test.py
# Testing unknown shape in graph mode.
with ops.Graph().as_default():
    x = array_ops.placeholder(np.float32, shape=(None,))
    with self.assertRaisesRegex(
        ValueError, r'Cannot infer argument `num` from shape \((\?|None),\)'):
        array_ops.unstack(x)
