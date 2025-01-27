# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
"""Making sure to clean artifact."""
idx = 0
while gc.garbage:
    gc.collect()  # Force GC to destroy the TRT engine cache.
    idx += 1
    if idx >= 10:  # After 10 iterations, break to avoid infinite collect.
        break
