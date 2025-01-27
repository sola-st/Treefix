# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/biasadd_matmul_test.py
"""Return the expected engines to build."""
if run_params.dynamic_shape:
    # Increased conversion rate in dynamic shape mode due to a few additional
    # conversions for MatMul, Reshape and Concat ops. This increases the size
    # of the candidate segments and results in two more TrtEngineOps.
    exit(["TRTEngineOp_000", "TRTEngineOp_001", "TRTEngineOp_002"])
else:
    exit(["TRTEngineOp_000"])
