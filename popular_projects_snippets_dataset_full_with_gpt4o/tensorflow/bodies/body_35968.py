# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with variable_scope.variable_scope(
    "scope0", partitioner=axis0_into2_partitioner):
    variable_scope.get_variable("name0", shape=(3, 1, 1))

with variable_scope.variable_scope(
    "scope0", partitioner=axis0_into3_partitioner, reuse=True):
    with self.assertRaisesRegex(
        ValueError,
        "Trying to reuse partitioned variable .* but specified partitions "
        ".* and found partitions .*"):
        variable_scope.get_variable("name0", shape=(3, 1, 1))

with variable_scope.variable_scope(
    "scope0", partitioner=axis0_into1_partitioner, reuse=True):
    with self.assertRaisesRegex(
        ValueError,
        "Trying to reuse partitioned variable .* but specified partitions "
        ".* and found partitions .*"):
        variable_scope.get_variable("name0", shape=(3, 1, 1))
