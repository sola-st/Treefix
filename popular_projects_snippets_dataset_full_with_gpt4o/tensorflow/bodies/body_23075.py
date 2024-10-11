# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
"""Setup method."""
super().setUp()
warnings.simplefilter("always")

if not is_tensorrt_enabled():
    self.skipTest("Test requires TensorRT")
