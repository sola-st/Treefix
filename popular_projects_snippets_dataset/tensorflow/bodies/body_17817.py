# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
with ops.Graph().as_default():
    pfor_outputs, while_outputs = create_lstm_per_eg_grad(100, 32, 8)
    self._run(pfor_outputs, 100, name="lstm_per_eg_grad_pfor")
    self._run(while_outputs, 20, name="lstm_per_eg_grad_while")
