# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
# This test makes sure consecutive variable reads don't copy
# the underlying memory.
with self.test_scope():
    # Create 128MiB variables
    var = resource_variable_ops.ResourceVariable(
        array_ops.ones([32, 1024, 1024]))

    # Read the same variable 100 times. If the underlying tensor
    # is not copied, this is a trivial operation. If it is copied,
    # this will eat over 13GB and OOM.
    values = []
    for _ in range(100):
        values.append(var.value())
