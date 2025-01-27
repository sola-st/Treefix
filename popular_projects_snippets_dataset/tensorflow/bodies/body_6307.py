# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
exit(strategy.extended._batch_gather_to(  # pylint: disable=protected-access
    [(v, _batch_reduce_destination(v)) for v in value_flat], axis,
    options))
