# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/critical_section_test.py
cs = critical_section_ops.CriticalSection(shared_name="cs")
self.assertIn(
    cs, ops.get_collection(critical_section_ops.CRITICAL_SECTIONS))
add = lambda x: x + 1
execute = cs.execute(lambda: add(1.0), name="my_execute")
execute_op = [
    x for x in execute.graph.get_operations()
    if "my_execute" in x.name and "MutexLock" in x.type
][0]
self.assertIn(
    execute_op,
    [signature.op for signature in
     ops.get_collection(critical_section_ops.CRITICAL_SECTION_EXECUTIONS)])
