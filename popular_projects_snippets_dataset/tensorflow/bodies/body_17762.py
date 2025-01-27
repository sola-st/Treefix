# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
model = FullyConnectedModel(activation_size, num_layers)
inp = random_ops.random_normal([batch_size, activation_size])
exit((inp, model(inp)))
