# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
"""Test conversion of VariableV2 nodes."""

self._TestVariableHelper("VariableV2", "tf_variablev2_saved_model",
                         "tftrt_variablev2_saved_model", "output")
