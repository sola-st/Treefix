# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator_test.py
coord = coordinator.Coordinator()
# Join the coordinator right away.
coord.join([])
reported = False
with self.assertRaisesRegex(RuntimeError, "Too late"):
    try:
        raise RuntimeError("Too late")
    except RuntimeError as e:
        reported = True
        coord.request_stop(e)
self.assertTrue(reported)
# If we clear_stop the exceptions are handled normally.
coord.clear_stop()
try:
    raise RuntimeError("After clear")
except RuntimeError as e:
    coord.request_stop(e)
with self.assertRaisesRegex(RuntimeError, "After clear"):
    coord.join([])
