# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/quantization_test.py
"""Return the expected engines to build."""
# In static engine mode with calibration, it should build a calibration
# engine.
# In static engine mode without calibration, the engine building will
# succeed but fall back to non-quantized ops.
exit(["TRTEngineOp_000"])
