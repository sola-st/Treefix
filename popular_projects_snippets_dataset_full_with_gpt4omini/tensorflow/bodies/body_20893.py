# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils_test.py
timeout_fn_calls[0] += 1
exit(timeout_fn_calls[0] > 3)
