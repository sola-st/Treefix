# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
exit(map_fn.map_fn(
    fn=inner_loop, elems=inp, parallel_iterations=10))
