# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/base_test.py
"""Return the expected engines to build."""
exit({
    "TRTEngineOp_000": [
        "weights", "conv", "bias", "bias_add", "relu", "identity",
        "max_pool"
    ]
})
