# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
context = distribute_coordinator_context.get_current_worker_context()
self.assertTrue(context is not None)
with self._test_session(target=context.master_target) as sess:
    xs = []
    expected = 0.0
    for i in range(context.num_workers):
        with ops.device("/job:worker/task:%d" % i):
            x = variable_scope.get_variable("x_%d" % i, initializer=10.0)
            x_add = x.assign_add(float(i))
            xs.append(x_add)
            expected += i + 10.0

    with ops.device("/job:worker/task:0"):
        result = math_ops.add_n(xs)

    self.evaluate(variables.global_variables_initializer())
    result_value = sess.run(result)
self.assertEqual(result_value, expected)
if result_value == expected:
    self._result_correct += 1
