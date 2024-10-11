# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/reduce_join_op_test.py
input_array = [["a"], ["b"]]
truth = ["ab"]
truth_shape = None
with self.cached_session():
    placeholder = array_ops.placeholder(dtypes.string, name="placeholder")
    reduced = string_ops.reduce_join(placeholder, axis=0)
    output_array = reduced.eval(feed_dict={placeholder.name: input_array})
    self.assertAllEqualUnicode(truth, output_array)
    self.assertAllEqual(truth_shape, reduced.get_shape())
