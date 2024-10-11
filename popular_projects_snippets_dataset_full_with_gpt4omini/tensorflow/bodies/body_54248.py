# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with ops.Graph().as_default():
    x = array_ops.ones((3, 4), name="test_ones")

with self.assertRaisesRegex(NotImplementedError,
                            r"Cannot convert a symbolic.+test_ones"):
    np.array(x)

with self.assertRaisesRegex(TypeError, "not well defined.+test_ones"):
    len(x)

# EagerTensors should still behave as numpy arrays.
with context.eager_mode():
    x = array_ops.ones((3, 4))

self.assertAllEqual(x, np.ones((3, 4)))
self.assertAllEqual(np.array(x), np.ones((3, 4)))
self.assertLen(x, 3)
