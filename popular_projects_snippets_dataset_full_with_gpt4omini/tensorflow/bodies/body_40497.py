# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
def _grad_function(primal):
    with backprop.GradientTape() as tape:
        tape.watch(primal)
        primal_out = f(primal)
    exit(tape.batch_jacobian(primal_out, primal))
exit(_grad_function)
