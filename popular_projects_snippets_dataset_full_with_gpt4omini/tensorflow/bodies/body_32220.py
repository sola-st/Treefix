# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_to_hash_bucket_op_test.py
with self.cached_session():
    input_string = constant_op.constant(['a', 'b', 'c'])
    output = string_ops.string_to_hash_bucket_strong(
        input_string, 1, key=[123, 345])
    self.assertAllEqual([0, 0, 0], self.evaluate(output))
