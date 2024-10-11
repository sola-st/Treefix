# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
pfor_outputs, while_outputs = create_lstm_per_eg_grad(8, 4, 2)
self.run_and_assert_equal(pfor_outputs, while_outputs)
