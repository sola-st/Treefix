# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
cond.acquire()
# Ensure that all threads set their mode simultaneously
# Note that this is not a simple assignment, as the execution_mode is an
# @property with a custom setter.
ctx.execution_mode = mode
count[0] = count[0] + 1
if count[0] < num_threads:
    cond.wait()
else:
    cond.notify_all()
cond.release()
self.assertEqual(ctx.execution_mode, mode)
