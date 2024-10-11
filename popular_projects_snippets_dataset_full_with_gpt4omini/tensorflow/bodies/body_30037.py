# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/weights_broadcast_test.py
static_op = weights_broadcast_ops.broadcast_weights(
    weights=weights, values=values)
weights_placeholder = array_ops.placeholder(dtypes_lib.float32)
values_placeholder = array_ops.placeholder(dtypes_lib.float32)
dynamic_op = weights_broadcast_ops.broadcast_weights(
    weights=weights_placeholder, values=values_placeholder)
with self.cached_session():
    self.assertAllEqual(expected, self.evaluate(static_op))
    self.assertAllEqual(expected, dynamic_op.eval(feed_dict={
        weights_placeholder: weights,
        values_placeholder: values,
    }))
