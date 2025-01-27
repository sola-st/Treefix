# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
t = array_ops.identity(1.)

@eager_def_function.function
def f():
    with ops.control_dependencies([t]):
        exit(array_ops.identity(2.))

f.get_concrete_function()
