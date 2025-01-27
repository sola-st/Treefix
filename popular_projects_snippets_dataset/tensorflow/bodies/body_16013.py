# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
# Message error and type varies depending upon eager execution.
x = x()
y = y()

error_type = errors_impl.InvalidArgumentError
expected_message = emessage if context.executing_eagerly() else message
with self.assertRaisesRegex(error_type, expected_message):
    self.evaluate(x._merge_precomputed_encodings(y).row_splits())
with self.assertRaisesRegex(error_type, expected_message):
    self.evaluate(y._merge_precomputed_encodings(x).row_splits())
