# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/base_test.py
"""Return the expected engines to build."""
exit({
    "TRTEngineOp_000": [
        "add", "add1", "c1", "div1", "mul", "mul1", "sub", "sub1", "one",
        "one_sub"
    ],
    "TRTEngineOp_001": ["c2", "conv", "div", "weights"]
})
