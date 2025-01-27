# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/strings_reduce_join_op_test.py
input_array = [b'this', b'is', b'a', b'test']
truth = b'thisisatest'
truth_shape = []
with self.cached_session():
    output = ragged_string_ops.reduce_join(
        inputs=input_array, axis=-1, keepdims=False, separator='')
    output_array = self.evaluate(output)
self.assertAllEqual(truth, output_array)
self.assertAllEqual(truth_shape, output.get_shape())
