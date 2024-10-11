# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_to_hash_bucket_op_test.py
with self.cached_session():
    input_string = array_ops.placeholder(dtypes.string)
    output = string_ops.string_to_hash_bucket(input_string, 10)
    result = output.eval(feed_dict={input_string: ['a', 'b', 'c']})

    # Hash64('a') -> 2996632905371535868 -> mod 10 -> 8
    # Hash64('b') -> 5795986006276551370 -> mod 10 -> 0
    # Hash64('c') -> 14899841994519054197 -> mod 10 -> 7
    self.assertAllEqual([8, 0, 7], result)
