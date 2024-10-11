# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = resource_variable_ops.ResourceVariable([0, 1, 2, 3], name="update")
# The exact error and message differ between graph construction (where the
# error is realized during shape inference at graph construction time),
# eager execution (where the error is realized during kernel execution),
# and XLA auto-clustering execution (where the error is realized in the xla
# op kernel) which is triggered when running in eager op as function mode.
with self.assertRaisesRegex(Exception, r"shape.*2.*3|RET_CHECK failure"):
    state_ops.scatter_update(v, [0, 1], [0, 1, 2])
