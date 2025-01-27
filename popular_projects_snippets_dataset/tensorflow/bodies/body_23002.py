# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/base_test.py
"""Return the expected engines to build."""
exit({
    "TRTEngineOp_000": ["c0", "c1", "add0", "add1", "mul0", "mul1"],
    "TRTEngineOp_001": ["c2", "c3", "add2", "add3", "mul2", "mul3"]
})
