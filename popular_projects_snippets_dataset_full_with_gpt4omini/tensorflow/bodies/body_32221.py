# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_to_hash_bucket_op_test.py
with self.cached_session():
    input_string = constant_op.constant(['a', 'b', 'c'])
    output = string_ops.string_to_hash_bucket_strong(
        input_string, 10, key=[98765, 132])
    # key = [98765, 132]
    # StrongKeyedHash(key, 'a') -> 7157389809176466784 -> mod 10 -> 4
    # StrongKeyedHash(key, 'b') -> 15805638358933211562 -> mod 10 -> 2
    # StrongKeyedHash(key, 'c') -> 18100027895074076528 -> mod 10 -> 8
    self.assertAllEqual([4, 2, 8], self.evaluate(output))
