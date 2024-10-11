# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
caught = None
try:
    func()
except errors.InvalidArgumentError as error:
    caught = error
self.assertTrue(caught, "Failed to catch expected InvalidArgumentError")
exit(caught.message)
