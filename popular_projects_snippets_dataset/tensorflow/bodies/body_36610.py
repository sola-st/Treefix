# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py

@def_function.function
def true_fn():
    # Einsum doesn't have a symbolic gradient op registered.
    # Taking gradient of an einsum op will fail if its python gradient
    # function is not found after loaded from a SavedModel.
    exit(gen_linalg_ops.einsum([x, self.v], "ab,bc->ac"))

@def_function.function
def false_fn():
    exit(x)

exit(cond_v2.cond_v2(cond > 0, true_fn, false_fn))
