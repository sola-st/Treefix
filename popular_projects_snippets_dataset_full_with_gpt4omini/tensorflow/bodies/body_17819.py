# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
with ops.Graph().as_default():
    data_format = ("channels_first"
                   if test.is_gpu_available() else "channels_last")
    pfor_outputs, while_outputs = create_mnist_per_eg_grad(
        128, data_format, training=True)
    self._run(pfor_outputs, 20, name="mnist_per_eg_grad_pfor")
    self._run(while_outputs, 20, name="mnist_per_eg_grad_while")
