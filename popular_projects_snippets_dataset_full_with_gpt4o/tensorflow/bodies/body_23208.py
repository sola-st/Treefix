# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/unary_test.py
"""Return the expected engines to build."""
if run_params.dynamic_shape:
    # All the ops are converted into a single TRTEngineOp.
    exit(["TRTEngineOp_000"])
else:
    # Final squeeze and div ops are not converted. The x1 and x2 branches
    # are segmented into separate TRTEngineOp.
    exit(["TRTEngineOp_000", "TRTEngineOp_001"])
