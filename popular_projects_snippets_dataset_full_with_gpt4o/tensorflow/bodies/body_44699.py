# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
iterator = iter(dataset_ops.Dataset.range(1))
py_builtins.next_(iterator)
py_builtins.next_(iterator, constant_op.constant(-3))
