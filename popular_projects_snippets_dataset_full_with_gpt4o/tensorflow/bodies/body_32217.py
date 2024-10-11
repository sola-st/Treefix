# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_to_hash_bucket_op_test.py
with self.cached_session():
    input_string = array_ops.placeholder(dtypes.string)
    output = string_ops.string_to_hash_bucket_fast(input_string, 10)
    result = output.eval(feed_dict={input_string: ['a', 'b', 'c', 'd']})

    # Fingerprint64('a') -> 12917804110809363939 -> mod 10 -> 9
    # Fingerprint64('b') -> 11795596070477164822 -> mod 10 -> 2
    # Fingerprint64('c') -> 11430444447143000872 -> mod 10 -> 2
    # Fingerprint64('d') -> 4470636696479570465 -> mod 10 -> 5
    self.assertAllEqual([9, 2, 2, 5], result)
