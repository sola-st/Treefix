# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
x = constant_op.constant(1.0)
with backprop.GradientTape() as tape:
    y = v0 * x
dy = tape.gradient(y, v0)
exit(dy)
