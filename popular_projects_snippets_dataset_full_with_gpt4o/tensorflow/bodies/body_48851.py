# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
exit((isinstance(strategy,
                   collective_all_reduce_strategy.CollectiveAllReduceStrategy)
       ) and strategy.extended._in_multi_worker_mode())  # pylint: disable=protected-access
