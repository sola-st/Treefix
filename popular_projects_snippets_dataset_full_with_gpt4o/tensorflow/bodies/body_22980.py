# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_function_test.py
"""Return the expected engines to build."""
exit({
    "TRTEngineOp_000": [
        "weights", "conv", "bias", "bias_add", "relu", "identity",
        "max_pool"
    ]
})
