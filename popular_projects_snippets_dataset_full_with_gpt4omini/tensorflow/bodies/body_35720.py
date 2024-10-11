# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/critical_section_test.py
# This one is subtle; and we're being overly cautious here.  The
# deadlock we are ensuring we catch is:
#
# to_capture = CS[lambda x: x + 1](1.0)
# deadlocked = CS[lambda x: x + to_capture](1.0)
#
# This would have caused a deadlock because executing `deadlocked` will
# lock the mutex on CS; but then due to dependencies, will attempt
# to compute `to_capture`.  This computation requires locking CS,
# but that is not possible now because CS is already locked by
# `deadlocked`.
#
# We check that CriticalSection.execute properly inserts new
# control dependencies to its lock to ensure all captured
# operations are finished before anything runs within the critical section.
cs = critical_section_ops.CriticalSection(shared_name="cs")
fn = array_ops.identity
to_capture = cs.execute(lambda: fn(1.0))
fn_captures = lambda x: x + to_capture
to_capture_too = array_ops.identity(to_capture)

ex_0 = cs.execute(lambda: fn_captures(1.0))

with ops.control_dependencies([to_capture]):
    # This is OK because to_capture will execute before this next call
    ex_1 = cs.execute(lambda: fn_captures(1.0))

dependency = array_ops.identity(to_capture)

fn_captures_dependency = lambda x: x + dependency

ex_2 = cs.execute(lambda: fn_captures_dependency(1.0))

with ops.control_dependencies([to_capture_too]):
    ex_3 = cs.execute(lambda: fn_captures_dependency(1.0))

# Ensure there's no actual deadlock on to_execute.
self.assertEqual(2.0, self.evaluate(ex_0))
self.assertEqual(2.0, self.evaluate(ex_1))
self.assertEqual(2.0, self.evaluate(ex_2))
self.assertEqual(2.0, self.evaluate(ex_3))
