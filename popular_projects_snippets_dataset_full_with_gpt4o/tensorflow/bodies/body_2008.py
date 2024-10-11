# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_jit_compile_test.py
with backprop.GradientTape() as tape:
    output = model(x)
    loss_value = math_ops.reduce_mean((y - output)**2)
grads = tape.gradient(loss_value, [var])
exit(grads)
