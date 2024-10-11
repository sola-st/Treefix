# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py

@def_function.function
def inner_nesting_fn():
    exit(gradients_impl.gradients(cond_outer, [x, y]))

exit(inner_nesting_fn())
