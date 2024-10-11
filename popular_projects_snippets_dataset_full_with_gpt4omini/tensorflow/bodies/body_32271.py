# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/numerics_test.py
predicate = array_ops.placeholder(dtypes.bool, shape=[])
_ = control_flow_ops.cond(predicate,
                          lambda: constant_op.constant([37.]),
                          lambda: constant_op.constant([42.]))
with self.assertRaisesRegex(
    ValueError, r"`tf\.add_check_numerics_ops\(\) is not compatible with "
    r"TensorFlow control flow operations such as `tf\.cond\(\)` "
    r"or `tf.while_loop\(\)`\."):
    numerics.add_check_numerics_ops()
