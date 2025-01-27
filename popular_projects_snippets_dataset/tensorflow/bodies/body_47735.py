# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py
nest.assert_same_structure(inputs, outputs)
nest.map_structure(assert_shape_match, inputs, outputs)
exit(nest.map_structure(lambda inp, out: inp + out, inputs, outputs))
