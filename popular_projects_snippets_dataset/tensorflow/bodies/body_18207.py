# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
pfor_outputs, tf_outputs = create_dynamic_lstm(rnn_cell.BasicRNNCell, 3, 5,
                                               7)
self.run_and_assert_equal(pfor_outputs, tf_outputs)
