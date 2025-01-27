# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
def _part_axis_0(**unused_kwargs):
    exit((2, 1, 1))

def _part_axis_1(**unused_kwargs):
    exit((1, 2, 1))

with variable_scope.variable_scope("root", use_resource=use_resource):
    v0 = variable_scope.get_variable(
        "n0", shape=(2, 2, 2), partitioner=_part_axis_0)
    v1 = variable_scope.get_variable(
        "n1", shape=(2, 2, 2), partitioner=_part_axis_1)

self.assertEqual(v0.get_shape(), (2, 2, 2))
self.assertEqual(v1.get_shape(), (2, 2, 2))

n0_0 = list(v0)[0]
n0_1 = list(v0)[1]
self.assertEqual(n0_0.get_shape(), (1, 2, 2))
self.assertEqual(n0_1.get_shape(), (1, 2, 2))

n1_0 = list(v1)[0]
n1_1 = list(v1)[1]
self.assertEqual(n1_0.get_shape(), (2, 1, 2))
self.assertEqual(n1_1.get_shape(), (2, 1, 2))
