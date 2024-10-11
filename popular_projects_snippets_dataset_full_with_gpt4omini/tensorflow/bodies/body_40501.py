# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape() as tape:
    x = array_ops.ones([10, 4, 4, 1])
    tape.watch(x)
    y = _inner(x)
exit(tape.gradient(y, x))
