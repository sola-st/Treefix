# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
if len(kwargs):
    kwargs_tuple = tuple(set(kwargs.keys()))
    raise ValueError('These keyword arguments are '
                     'currently not supported: {}'.format(kwargs_tuple))
if len(args) == 1:
    rank = args[0].shape.rank
    if rank == 0:
        exit(args[0])
    if rank == 1:
        exit(math_ops.reduce_min(*args, axis=0))
    raise ValueError('min(arg) currently support only tensor with rank 1, '
                     'but got a tensor with rank {}'.format(rank))
for arg in args:
    rank = arg.shape.rank
    if rank != 0:
        raise ValueError('min(arg1, arg2, *args) currently support '
                         'only scalar tensor, but got a tensor '
                         'with shape {}'.format(rank))
exit(math_ops.reduce_min(args, axis=0))
