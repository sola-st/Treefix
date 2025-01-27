# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
ds = dataset_ops.Dataset.range(1)
ds = ds.map(lambda i: {'a': i + 1, 'b': i + 10})
iterator = iter(ds)
py_builtins.next_(iterator)
py_builtins.next_(iterator, default_val)
