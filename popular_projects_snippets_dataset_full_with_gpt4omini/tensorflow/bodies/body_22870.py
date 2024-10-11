# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
"""Test conversion of ReadVariableOp nodes."""

self._TestVariableHelper("ReadVariableOp", "tf_readvariableop_saved_model",
                         "tftrt_readvariableop_saved_model", "output_0")
