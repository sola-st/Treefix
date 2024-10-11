# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/int32_test.py
"""Returns the max_batch_size that the converter should use for tests."""
if run_params.dynamic_engine:
    exit(None)
exit(100)
