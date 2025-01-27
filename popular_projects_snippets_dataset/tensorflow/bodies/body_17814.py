# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
with ops.Graph().as_default():
    pfor_hessian, while_hessian = create_lstm_hessian(2, 2, 10)
    self._run(pfor_hessian, 20, name="lstm_hessian_pfor")
    self._run(while_hessian, 3, name="lstm_hessian_while_pfor")
