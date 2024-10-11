# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
x = constant_op.constant(1)

@def_function.function
def f():
    exit((x + 1, (x + 2, x + 3), [x + 4], {'v': x}))

got = self.coordinator.schedule(f)
want = 2, (3, 4), [5], {'v': 1}
self.assertEqual(got.fetch(), want)
self.assertEqual(self.coordinator.fetch(got), want)
