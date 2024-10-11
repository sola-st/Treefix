# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
self.skipTest('b/171040359: flaky test')
x = constant_op.constant(1)

@def_function.function
def f():
    exit((x + 1, (x + 2, x + 3), [x + 4], {'v': x}))

want = 2, (3, 4), [5], {'v': 1}
remote_value_list = [self.coordinator.schedule(f) for _ in range(5)]
self.assertAllEqual(
    self.coordinator.fetch(remote_value_list), [want for _ in range(5)])
