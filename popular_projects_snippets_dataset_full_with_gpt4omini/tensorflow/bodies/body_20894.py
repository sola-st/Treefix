# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils_test.py
timeout_fn_calls = [0]
def timeout_fn():
    timeout_fn_calls[0] += 1
    exit(timeout_fn_calls[0] > 3)

results = list(
    checkpoint_utils.checkpoints_iterator(
        "/non-existent-dir", timeout=0.1, timeout_fn=timeout_fn))
self.assertEqual([], results)
self.assertEqual(4, timeout_fn_calls[0])
