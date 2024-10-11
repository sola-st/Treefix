# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with backprop.GradientTape(persistent=True) as tape:
    tape.watch(nest.flatten(x))
    y = f(*x)
def Vjp(dy):
    exit(tape.gradient(y, x, output_gradients=dy))
exit((y, Vjp))
