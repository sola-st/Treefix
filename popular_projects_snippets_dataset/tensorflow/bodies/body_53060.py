# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
seq = array_ops.split(x, 3, 0)
exit(rnn.static_rnn(
    cell, seq, dtype=dtypes.float32, sequence_length=[1]))
