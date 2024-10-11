# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
err_msg = 'row_splits tensor may not be empty'
with self.assertRaisesRegex(ValueError, err_msg):
    RaggedTensor.from_row_splits([], [])
