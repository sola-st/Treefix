# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape(persistent=True) as tape:
    tape.watch(x)
    y = x**2
exit(tape.batch_jacobian(y, x, experimental_use_pfor=use_pfor))
