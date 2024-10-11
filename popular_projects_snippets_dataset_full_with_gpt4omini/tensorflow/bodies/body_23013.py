# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/base_test.py
"""Return the expected engines to build."""
exit({
    "TRTEngineOp_000": ["add2", "add3", "mul1"],
    # Why segment ["add", "add1", "mul"] was assigned segment id 1
    # instead of 0: the parent node of this segment is actually const
    # node 'c', but it's removed later since it's const output of the
    # segment which is not allowed.
    "TRTEngineOp_001": ["add", "add1", "mul"]
})
