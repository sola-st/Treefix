# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
with self.assertRaisesRegex(ValueError, 'must be greater than 1'):
    RaggedTensor.from_tensor(tensor)
