# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/critical_section_test.py
c = v.read_value()
def true_fn():
    with ops.control_dependencies([c]):
        nv = v.assign_add(a * b)
        with ops.control_dependencies([nv]):
            exit(array_ops.identity(c))
exit(control_flow_ops.cond(
    array_ops.identity(inner_cond), true_fn, lambda: c))
