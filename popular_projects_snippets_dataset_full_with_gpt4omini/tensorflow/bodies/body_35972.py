# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with variable_scope.variable_scope(
    "scope0", partitioner=axis0_into2_partitioner) as vs:
    self.assertEqual(axis0_into2_partitioner, vs.partitioner)
    with variable_scope.variable_scope(vs) as vs1:
        self.assertEqual(axis0_into2_partitioner, vs1.partitioner)
