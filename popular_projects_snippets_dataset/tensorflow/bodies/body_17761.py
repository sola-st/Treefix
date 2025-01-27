# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
activation = inp
for layer in self._layers:
    activation = layer(activation)
exit(activation)
