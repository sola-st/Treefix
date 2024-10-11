# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/base_test.py
"""Return the expected engines to build."""
exit({
    "TRTEngineOp_000": ["add", "add1", "mul"],
    "TRTEngineOp_001": ["add2", "add3", "mul1"]
})
