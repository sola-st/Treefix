# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape() as tape:
    tape.watch([a, b])
    y = a**3
    z = b**2
exit(tape.gradient([y, z], [a, b]))
