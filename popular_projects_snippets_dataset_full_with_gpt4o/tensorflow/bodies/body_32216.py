# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_to_hash_bucket_op_test.py
with self.cached_session():
    input_string = array_ops.placeholder(dtypes.string)
    output = string_ops.string_to_hash_bucket_fast(input_string, 1)
    result = output.eval(feed_dict={input_string: ['a', 'b', 'c']})

    self.assertAllEqual([0, 0, 0], result)
