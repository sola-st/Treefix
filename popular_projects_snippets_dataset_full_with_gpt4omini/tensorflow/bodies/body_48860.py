# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
exit((isinstance(obj, ds_values.DistributedValues) and
        isinstance(obj, composite_tensor.CompositeTensor)))
