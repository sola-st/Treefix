# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/neighboring_engine_test.py
"""Return the expected engines to build."""
exit({
    "TRTEngineOp_000": ["bias", "mul", "sub"],
    "TRTEngineOp_001": ["weights", "conv"]
})
