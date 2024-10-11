# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
x = constant_op.constant([3.14, 2.68, 7.69])
with backprop.GradientTape() as tape:
    tape.watch(x)
    y = f(x)
    exit(tape.gradient(y, x))
