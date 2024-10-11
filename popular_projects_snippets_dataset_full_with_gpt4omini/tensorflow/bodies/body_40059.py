# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
with backprop.GradientTape() as tape:
    tape.watch(params)
    primals_out = f(*params)
exit(tape.gradient(
    primals_out,
    params[argnums],
    unconnected_gradients=UnconnectedGradients.ZERO))
