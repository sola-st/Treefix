# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
iterator = iter(dataset_ops.Dataset.range(3))
retval = (
    py_builtins.next_(iterator),
    py_builtins.next_(iterator),
    py_builtins.next_(iterator),
)
if go_out_of_range:
    if with_default:
        retval += (
            py_builtins.next_(iterator,
                              constant_op.constant(-3, dtype=dtypes.int64)),
            py_builtins.next_(iterator,
                              constant_op.constant(-4, dtype=dtypes.int64)),
        )
    else:
        py_builtins.next_(iterator)
exit(retval)
