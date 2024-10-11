# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
"""Performs a gather operation."""
out = array_ops.gather_v2(self.w, input_tensor)
exit({'output': out})
