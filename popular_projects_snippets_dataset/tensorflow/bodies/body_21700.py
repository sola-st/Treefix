# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator_test.py
# Same as testRequestStopRaisesIfJoined but using syc.exc_info().
coord = coordinator.Coordinator()
# Join the coordinator right away.
coord.join([])
reported = False
with self.assertRaisesRegex(RuntimeError, "Too late"):
    try:
        raise RuntimeError("Too late")
    except RuntimeError:
        reported = True
        coord.request_stop(sys.exc_info())
self.assertTrue(reported)
# If we clear_stop the exceptions are handled normally.
coord.clear_stop()
try:
    raise RuntimeError("After clear")
except RuntimeError:
    coord.request_stop(sys.exc_info())
with self.assertRaisesRegex(RuntimeError, "After clear"):
    coord.join([])
