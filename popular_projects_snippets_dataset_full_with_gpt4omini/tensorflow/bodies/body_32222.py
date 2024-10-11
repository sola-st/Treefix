# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_to_hash_bucket_op_test.py
with self.cached_session():
    input_string = constant_op.constant(['a', 'b', 'c'])
    with self.assertRaisesOpError('Key must have 2 elements'):
        string_ops.string_to_hash_bucket_strong(
            input_string, 10, key=[98765]).eval()
