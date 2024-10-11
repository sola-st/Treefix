# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
seq = tf.split(x, 3, 0)
exit(rnn.static_rnn(cell, seq, dtype=tf.float32, sequence_length=[1]))
