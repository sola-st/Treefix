# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/reduce_join_op_test.py
with self.cached_session():
    placeholder = array_ops.placeholder(dtypes.int32, name="placeholder")
    reduced = string_ops.reduce_join(["test", "test2"], axis=placeholder)

    with self.assertRaisesOpError("reduction dimension -2"):
        reduced.eval(feed_dict={placeholder.name: -2})
    with self.assertRaisesOpError("reduction dimension 2"):
        reduced.eval(feed_dict={placeholder.name: 2})
