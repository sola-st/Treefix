# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py
shape = convert_to_batch_shape(s)
exit(random_ops.random_uniform(shape, seed=inner_seed, dtype=dtype))
