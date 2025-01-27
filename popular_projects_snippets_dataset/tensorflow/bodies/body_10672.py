# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
if shared_name is None:
    self._name = (
        ops.get_default_graph().unique_name(self.__class__.__name__))
elif isinstance(shared_name, str):
    self._name = shared_name
else:
    raise ValueError(f"shared_name must be a string, got {shared_name}")

self._dtypes = dtypes

if shapes is not None:
    if len(shapes) != len(dtypes):
        raise ValueError("StagingArea shapes must be the same length as dtypes")
    self._shapes = [tensor_shape.TensorShape(s) for s in shapes]
else:
    self._shapes = [tensor_shape.unknown_shape() for _ in self._dtypes]

if names is not None:
    if len(names) != len(dtypes):
        raise ValueError("StagingArea names must be the same length as dtypes")
    self._names = names
else:
    self._names = None

self._capacity = capacity
self._memory_limit = memory_limit

# all get and put ops must colocate with this op
with ops.name_scope("%s_root" % self._name):
    self._coloc_op = control_flow_ops.no_op()
