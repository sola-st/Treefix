# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
with ops.device("/device:GPU:0"):
    t = _create_tensor("test string")
    self.assertIn("GPU", t.device)
