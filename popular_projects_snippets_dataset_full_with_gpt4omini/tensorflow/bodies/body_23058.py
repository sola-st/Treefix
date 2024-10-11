# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/binary_tensor_weight_broadcast_test.py
"""Return the expected engines to build."""
# The final reshape op is converted only in dynamic shape mode. This op is
# placed into a new engine due to the preceding trt_incompatible_ops.
num_engines = 17 if run_params.dynamic_shape else 16
exit([f"TRTEngineOp_{i:03d}" for i in range(num_engines)])
