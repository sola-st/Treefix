# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/shape_output_test.py
"""Returns the expected engines to build."""
if run_params.dynamic_shape:
    exit(["TRTEngineOp_000"])
else:
    exit([])
