# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
exit(_generate_dropout_mask(
    array_ops.ones_like(inputs),
    self.dropout,
    training=training,
    count=count))
