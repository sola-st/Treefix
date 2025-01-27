# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
# Errors that are caught by runtime value checks.
x = x()
y = y()
with self.assertRaisesRegex(errors.InvalidArgumentError, message):
    self.evaluate(x._merge_precomputed_encodings(y).row_splits())
with self.assertRaisesRegex(errors.InvalidArgumentError, message):
    self.evaluate(y._merge_precomputed_encodings(x).row_splits())
