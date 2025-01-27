# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
dataset = dataset_ops.DatasetV2.range(5).filter(lambda _: True).batch(2)
exit(py_builtins.len_(dataset))
