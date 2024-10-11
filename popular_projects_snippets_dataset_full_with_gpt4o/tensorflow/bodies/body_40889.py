# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
x = ops.convert_to_tensor(x)
with backprop.GradientTape() as tape:
    tape.watch(x)
    y = f(x)
exit((y, tape.gradient(y, x)))
