# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/reshape_transpose_test.py
"""Return the expected engines to build."""
exit({
    "TRTEngineOp_000": ["reshape-%d" % i for i in range(7)] +
                       ["reshape-%d/shape" % i for i in range(7)]
})
