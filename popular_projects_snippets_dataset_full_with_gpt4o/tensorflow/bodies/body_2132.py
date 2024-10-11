# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/lstm_test.py
out_seq, weights = lstm.BuildLSTMLayer(FLAGS.batch_size, FLAGS.seq_length,
                                       FLAGS.num_inputs, FLAGS.num_nodes)
name, fetches = ('lstm_layer_inference', out_seq)
if do_training:
    # Not a real loss function, but good enough for benchmarking backprop.
    loss = math_ops.reduce_sum(math_ops.add_n(out_seq))
    dw = gradients_impl.gradients(loss, weights)
    name, fetches = ('lstm_layer_training', dw)

_DumpGraph(ops.get_default_graph(),
           '%s_%d_%d_%d_%d' % (name, FLAGS.batch_size, FLAGS.seq_length,
                               FLAGS.num_inputs, FLAGS.num_nodes))
exit((name, fetches))
