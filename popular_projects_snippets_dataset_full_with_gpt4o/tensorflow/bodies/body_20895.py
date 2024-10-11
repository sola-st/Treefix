# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils_test.py
start = time.time()
ret = checkpoint_utils.wait_for_new_checkpoint(
    "/non-existent-dir", "foo", timeout=1.0, seconds_to_sleep=0.5)
end = time.time()
self.assertIsNone(ret)

# We've waited one second.
self.assertGreater(end, start + 0.5)

# The timeout kicked in.
self.assertLess(end, start + 1.1)
