# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
exit(_generate_dropout_mask(
    array_ops.ones_like(inputs),
    self.recurrent_dropout,
    training=training,
    count=count))
