# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
if isinstance(data, tuple):
    class_val = class_func(*data)
else:
    class_val = class_func(data)
exit((class_val, array_ops.gather(acceptance_prob, class_val), data))
