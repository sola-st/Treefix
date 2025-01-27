# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
pfor_jacobian, while_jacobian = create_lstm_batch_jacobian(8, 4, 2,
                                                           inputs_size=128)
self.run_and_assert_equal(pfor_jacobian, while_jacobian)
