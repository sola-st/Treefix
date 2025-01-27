# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/quantization_test.py
"""Return the expected engines to build."""
# The fake quant ops are not supported in FP32/FP16 mode, and will split the
# graph into two TRT segments.
exit(["TRTEngineOp_000", "TRTEngineOp_001"])
