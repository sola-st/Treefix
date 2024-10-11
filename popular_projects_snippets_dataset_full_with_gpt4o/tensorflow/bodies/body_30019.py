# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/weights_broadcast_test.py
static_op = weights_broadcast_ops.assert_broadcastable(
    weights=weights, values=values)
weights_placeholder = array_ops.placeholder(dtypes_lib.float32)
values_placeholder = array_ops.placeholder(dtypes_lib.float32)
dynamic_op = weights_broadcast_ops.assert_broadcastable(
    weights=weights_placeholder, values=values_placeholder)
with self.cached_session():
    static_op.run()
    dynamic_op.run(feed_dict={
        weights_placeholder: weights,
        values_placeholder: values,
    })
