# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
if test_util.is_gpu_available():
    # TODO(allenl): Investigate possible GPU-specific memory leaks
    self.skipTest("Disabled when a GPU is available")
# TODO(kkb): Python memory checker complains continuous `weakref`
# allocations, investigate.
if memory_checker.CppMemoryChecker is None:
    self.skipTest("Requires the C++ memory checker")

def _create_and_delete_variable():
    resource_variable_ops.UninitializedVariable(
        shape=[100, 100],
        dtype=dtypes.float32)

_create_and_delete_variable()
checker = memory_checker.CppMemoryChecker(
    "ResourceVariableOps.testUninitializedVariableMemoryUsage")
for _ in range(2):
    _create_and_delete_variable()
    checker.record_snapshot()
checker.stop()
checker.report()
checker.assert_no_leak_if_all_possibly_except_one()
