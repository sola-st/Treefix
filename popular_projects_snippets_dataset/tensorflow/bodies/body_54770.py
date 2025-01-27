# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
# Scalar inputs.
tf_val = math_ops.not_equal(constant_op.constant(1),
                            constant_op.constant(1))
self.assertEqual(tensor_util.constant_value(tf_val), False)

tf_val = math_ops.not_equal(constant_op.constant(1),
                            constant_op.constant(0))
self.assertEqual(tensor_util.constant_value(tf_val), True)

# Shaped inputs with broadcast semantics.
tf_val = math_ops.not_equal(constant_op.constant([[0, 1]]),
                            constant_op.constant([[0], [1]]))
c_val = tensor_util.constant_value(tf_val)
self.assertAllEqual(c_val, [[False, True], [True, False]])
