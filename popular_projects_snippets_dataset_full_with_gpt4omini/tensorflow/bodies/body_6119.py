# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
exit([
    self.reduce_implementation(
        reduce_op, t, destinations=v, options=options)
    for t, v in value_destination_pairs
])
