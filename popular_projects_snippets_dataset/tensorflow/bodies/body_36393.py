# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
ops.reset_default_graph()
gc.collect()
initial_size = script_ops._py_funcs.size()

for _ in range(1000):
    make_graph()

ops.reset_default_graph()
gc.collect()
self.assertEqual(initial_size, script_ops._py_funcs.size())
