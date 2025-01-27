# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
self._layers = [
    tf_layers.Dense(activation_size, activation=nn.relu)
    for _ in range(num_layers)
]
