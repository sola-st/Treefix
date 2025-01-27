# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
self.distributed_variable = distributed_variable
self.components = (tuple(distributed_variable.shape.as_list()),
                   distributed_variable.dtype)
