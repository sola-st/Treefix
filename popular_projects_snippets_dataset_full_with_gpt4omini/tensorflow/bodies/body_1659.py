# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateless_random_ops_test.py
"""Tests all values of `alg`."""
if config.list_logical_devices('TPU') or config.list_logical_devices('GPU'):
    self.skipTest('Only _cpu tests linked in support for jit_compile on CPU.')
seed = [1, 2]
shape = [2, 3]
outputs = []
for alg in alg_group:
    with ops.device('CPU'):
        output = def_function.function(jit_compile=True)(op)(
            shape=shape, seed=seed, alg=alg)
    self.assertEqual(output.shape, shape)
    outputs.append(output)
x = outputs[0]
for y in outputs[1:]:
    self.assertAllEqual(x, y)
