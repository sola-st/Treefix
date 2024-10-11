# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
with backprop.GradientTape() as tape:
    tape.watch(primal)
    primal_out = f(primal)
exit(tape.gradient(primal_out, primal))
