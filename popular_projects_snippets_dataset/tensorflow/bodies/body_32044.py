# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_encode_op_test.py
with self.cached_session() as sess:
    value = sess.run(rt)
    if isinstance(value, np.ndarray):
        value = value.tolist()
    elif isinstance(value, ragged_tensor_value.RaggedTensorValue):
        value = value.to_list()
    self.assertEqual(value, expected)
