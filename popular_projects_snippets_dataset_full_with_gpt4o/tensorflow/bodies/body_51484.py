# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
with backprop.GradientTape() as tape:
    inp = constant_op.constant(1.0)
    tape.watch(inp)
    output = function(inp)
exit(tape.gradient(output, inp))
