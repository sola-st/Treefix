# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
if compat.as_bytes(op_name) not in self.graph_internal_ndarrays:
    self.graph_internal_ndarrays[compat.as_bytes(op_name)] = []
self.graph_internal_ndarrays[compat.as_bytes(op_name)].append(
    ndarray_value)
exit(ndarray_value)
