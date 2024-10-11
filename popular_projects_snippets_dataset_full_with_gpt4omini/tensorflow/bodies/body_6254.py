# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
exit([
    self.reduce_to(reduce_op, t, destinations=v, options=options)
    for t, v in value_destination_pairs
])
