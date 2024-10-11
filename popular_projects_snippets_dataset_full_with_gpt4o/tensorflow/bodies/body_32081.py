# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/reduce_join_op_test.py
with self.cached_session():
    placeholder = array_ops.placeholder(dtypes.string, name="placeholder")
    index_too_high = string_ops.reduce_join(placeholder, axis=1)
    duplicate_index = string_ops.reduce_join(placeholder, axis=[-1, 1])
    with self.assertRaisesOpError("Invalid reduction dimension 1"):
        index_too_high.eval(feed_dict={placeholder.name: [""]})
    with self.assertRaisesOpError("Duplicate reduction dimension 1"):
        duplicate_index.eval(feed_dict={placeholder.name: [[""]]})
