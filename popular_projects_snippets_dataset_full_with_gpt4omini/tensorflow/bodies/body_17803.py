# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
pfor_hessian, while_hessian = create_lstm_batch_hessian(2, 2, 2)
self.run_and_assert_equal(pfor_hessian, while_hessian)
