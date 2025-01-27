# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
with ops.Graph().as_default():
    pfor_jacobian, while_jacobian = create_lstm_batch_jacobian(
        100, 32, 8, inputs_size=128)
    self._run(pfor_jacobian, 100, name="lstm_batch_jacobian_pfor")
    self._run(while_jacobian, 20, name="lstm_batch_jacobian_while")
