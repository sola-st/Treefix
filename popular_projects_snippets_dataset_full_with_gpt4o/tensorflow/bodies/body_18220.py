# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
with ops.Graph().as_default():
    pfor_outputs, tf_outputs = create_dynamic_lstm(rnn_cell.BasicRNNCell, 128,
                                                   512, 16)
    self._run(pfor_outputs, 100, name="pfor_rnn")
    self._run(tf_outputs, 100, name="tf_rnn")
