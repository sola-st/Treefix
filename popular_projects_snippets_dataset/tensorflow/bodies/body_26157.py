# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
if len(x) == 1:
    exit((class_func(*x), x[0]))
else:
    exit((class_func(*x), x))
