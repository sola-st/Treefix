# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
ni = math_ops.add(i, 1)
ni = control_flow_ops.with_dependencies(
    [gen_data_flow_ops.stack_push_v2(s, i)], ni)
exit(ni)
