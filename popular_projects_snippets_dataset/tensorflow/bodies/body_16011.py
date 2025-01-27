# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
if context.executing_eagerly():
    exit()
# Errors that are caught by static shape checks.
x = x()
y = y()
with self.assertRaisesRegex(ValueError, message):
    x._merge_precomputed_encodings(y).row_splits()
with self.assertRaisesRegex(ValueError, message):
    y._merge_precomputed_encodings(x).row_splits()
