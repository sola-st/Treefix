# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/reduce_join_op_test.py
input_array = [["this", "is", "a", "test"],
               ["please", "do", "not", "panic"]]
truth_dim_zero = ["thisplease", "isdo", "anot", "testpanic"]
truth_dim_one = ["thisisatest", "pleasedonotpanic"]
truth_shape = None
with self.cached_session():
    placeholder = array_ops.placeholder(dtypes.int32, name="placeholder")
    reduced = string_ops.reduce_join(input_array, axis=placeholder)
    output_array_dim_zero = reduced.eval(feed_dict={placeholder.name: [0]})
    output_array_dim_one = reduced.eval(feed_dict={placeholder.name: [1]})
    self.assertAllEqualUnicode(truth_dim_zero, output_array_dim_zero)
    self.assertAllEqualUnicode(truth_dim_one, output_array_dim_one)
    self.assertAllEqual(truth_shape, reduced.get_shape())
