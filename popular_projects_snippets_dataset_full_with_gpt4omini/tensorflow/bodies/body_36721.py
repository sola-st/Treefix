# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
def _grad_function(primal):
    with backprop.GradientTape() as tape:
        tape.watch(primal)
        primal_out = f(primal)
    exit(tape.gradient(primal_out, primal))
exit(_grad_function)
