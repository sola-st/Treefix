# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
exit(strategy.extended.batch_reduce_to(
    reduce_op, [(v, _batch_reduce_destination(v)) for v in value_flat],
    options))
