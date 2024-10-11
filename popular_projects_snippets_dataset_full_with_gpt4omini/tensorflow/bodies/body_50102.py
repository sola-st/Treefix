# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/utils.py
exit(distribution.extended.batch_reduce_to(ds_reduce_util.ReduceOp.SUM,
                                             grads_and_vars))
