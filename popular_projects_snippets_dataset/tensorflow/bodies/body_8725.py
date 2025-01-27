# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
x = array_ops.identity(42.)
with backprop.GradientTape() as tape:
    tape.watch(x)
    y = comm_fn(x) * c
exit(tape.gradient(y, x))
