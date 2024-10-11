# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py

@def_function.function
def true_fn():
    exit(gen_linalg_ops.einsum([x, v], "ab,bc->ac"))

@def_function.function
def false_fn():
    exit(x)

exit(cond_v2.cond_v2(cond > 0, true_fn, false_fn))
