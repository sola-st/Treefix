# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
nonlocal num_traces
num_traces += 1
v = variables.Variable(3, experimental_enable_variable_lifting=False)
v.assign_add(5)
exit(v.read_value())
