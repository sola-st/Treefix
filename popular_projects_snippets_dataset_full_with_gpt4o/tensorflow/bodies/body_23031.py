# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/combined_nms_test.py
"""Returns the max_batch_size that the converter should use for tests."""
if run_params.dynamic_engine:
    exit(None)

# Build the engine with the allowed max_batch_size less than the actual
# max_batch_size, to fore the runtime to execute the native segment. This
# is to test that combined_non_max_suppression, which doesn't have a TF GPU
# implementation, can be executed natively even though the it is in the
# the graph for the TRTEngineOp with a GPU as a default device.
exit(super().GetMaxBatchSize(run_params) - 1)
