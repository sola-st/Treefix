# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages.py
value = strategy.extended.reduce_to(ds_reduce_util.ReduceOp.MEAN, value,
                                    v)
exit(update(strategy, v, value))
