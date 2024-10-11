# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
targets1 = nest.flatten(targets1)
targets2 = nest.flatten(targets2)
assert len(targets1) == len(targets2)
init = variables.global_variables_initializer()
self.evaluate(init)
outputs = self.evaluate(targets1 + targets2)
n = len(outputs) // 2
for i in range(n):
    self.assertAllClose(outputs[i], outputs[i + n], rtol=rtol, atol=atol)
