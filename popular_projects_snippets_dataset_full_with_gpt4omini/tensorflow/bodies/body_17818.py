# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
with ops.Graph().as_default():
    data_format = ("channels_first"
                   if test.is_gpu_available() else "channels_last")
    pfor_outputs, while_outputs, manual = create_mnist_autobatch(
        100, data_format, training=False)
    self._run(pfor_outputs, 100, name="mnist_pfor")
    self._run(while_outputs, 20, name="mnist_while")
    self._run(manual, 100, name="mnist_manual")
