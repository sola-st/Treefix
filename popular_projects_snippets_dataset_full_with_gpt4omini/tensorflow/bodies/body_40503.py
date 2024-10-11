# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape(persistent=True) as g:
    inp = random_ops.random_uniform([3, 2])
    g.watch(inp)
    output = nn.embedding_lookup(inp, [0, 2])
self.assertAllClose(
    g.jacobian(output, inp, experimental_use_pfor=True),
    g.jacobian(output, inp, experimental_use_pfor=False))
