# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with backprop.GradientTape() as tape:
    tape.watch(params)
    outputs = f(*params)
exit(tape.gradient(
    outputs,
    params[argnums],
    unconnected_gradients=unconnected_gradients.UnconnectedGradients.ZERO))
