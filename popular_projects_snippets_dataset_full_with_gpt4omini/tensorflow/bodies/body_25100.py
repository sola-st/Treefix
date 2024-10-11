# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
self.assertEqual(
    {"dtype": tensor.dtype, "shape": tensor.shape},
    annotations["tensor_metadata"])
