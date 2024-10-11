# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
with backprop.GradientTape() as tape:
    tape.watch(primal)
    primal_out = f(primal)
exit(tape.gradient(primal_out, primal))
