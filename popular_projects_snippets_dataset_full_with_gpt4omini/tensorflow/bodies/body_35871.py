# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/dense_update_ops_no_tsan_test.py
# We need each thread to keep its own device stack or the device scopes
# won't be properly nested.
ops.get_default_graph().switch_to_thread_local()
with self.cached_session() as sess:
    zeros_t = array_ops.fill([1024, 1024], 0.0)
    ones_t = array_ops.fill([1024, 1024], 1.0)
    p = variables.Variable(zeros_t)
    assigns = [
        state_ops.assign(
            p, math_ops.multiply(ones_t, float(i)), use_locking=True)
        for i in range(1, 21)
    ]
    self.evaluate(p.initializer)

    def run_assign(assign_op):
        self.evaluate(assign_op)

    threads = [
        self.checkedThread(
            target=run_assign, args=(assign_op,)) for assign_op in assigns
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    vals = self.evaluate(p)

    # Assert every element is the same, and taken from one of the assignments.
    self.assertTrue(vals[0, 0] > 0)
    self.assertTrue(vals[0, 0] <= 20)
    self.assertAllEqual(vals, np.ones([1024, 1024]) * vals[0, 0])
