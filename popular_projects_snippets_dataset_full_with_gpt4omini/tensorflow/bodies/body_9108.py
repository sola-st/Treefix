# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
context = distribute_coordinator_context.get_current_worker_context()
self.assertTrue(context is not None)
with ops.device("/job:ps/task:0"):
    # TODO(yuefengz): investigate why not using resource variable will make
    # the test flaky.
    x = variable_scope.get_variable("xx", initializer=10.0, use_resource=True)
with ops.device("/job:ps/task:1"):
    y = variable_scope.get_variable("yy", initializer=20.0, use_resource=True)

x_add = x.assign_add(2.0)
y_sub = y.assign_sub(2.0)
train_op = control_flow_ops.group([x_add, y_sub])

# The monitored session will run init or ready ops.
with monitored_session.MonitoredSession() as sess:
    sess.run(train_op)

    # Synchronize workers after one step to make sure they all have finished
    # training.
    if context.has_barrier:
        context.wait_for_other_workers()
    else:
        self._barrier.wait()

    x_val, y_val = sess.run([x, y])

self.assertEqual(x_val, 16.0)
self.assertEqual(y_val, 14.0)
if x_val == 16.0 and y_val == 14.0:
    with self._lock:
        self._result_correct += 1
