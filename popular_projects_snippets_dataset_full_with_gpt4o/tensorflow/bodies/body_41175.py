# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
with backprop.GradientTape() as tape:
    logits = constant_op.constant([1., 2.])
    tape.watch(logits)
    out = f(constant_op.constant(1), logits)
exit(tape.gradient(out, logits))
