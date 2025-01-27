# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
with ops.Graph().as_default():
    if test.is_gpu_available():
        data_format = "channels_first"
    else:
        data_format = "channels_last"
    pfor_outputs, while_outputs = create_mnist_per_eg_jacobian(
        16, data_format, training=True)
    self._run(pfor_outputs, 20, name="mnist_per_eg_jacobian_pfor")
    self._run(while_outputs, 20, name="mnist_per_eg_jacobian_while")
