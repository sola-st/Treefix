# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/reshape_transpose_test.py
"""Return the expected engines to build."""
exit({
    "TRTEngineOp_000": [
        "transpose-1", "transpose-1/perm", "transposeback",
        "transposeback/perm"
    ]
})
