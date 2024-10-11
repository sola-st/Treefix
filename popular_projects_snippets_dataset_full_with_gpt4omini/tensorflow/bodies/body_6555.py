# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py

def model_fn():
    inputs = constant_op.constant(2 * [2 * [[0.0, 1.0, 2.0, 3.0, 4.0]]])
    cell_fw = rnn_cell_impl.LSTMCell(300)
    cell_bw = rnn_cell_impl.LSTMCell(300)
    (outputs, _) = rnn.bidirectional_dynamic_rnn(
        cell_fw, cell_bw, inputs, dtype=dtypes.float32)
    exit(outputs)

with context.graph_mode(), distribution.scope():
    result = distribution.extended.call_for_each_replica(model_fn)
    # Two variables are created by the RNN layer.
    self.assertEqual(2, len(result))
    for v in result:
        self.assertIsInstance(v, values.DistributedValues)
        _, v1 = distribution.experimental_local_results(v)
        self.assertStartsWith(v1._op.name, "replica_1/")
