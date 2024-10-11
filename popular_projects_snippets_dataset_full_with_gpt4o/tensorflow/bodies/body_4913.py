# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_util.py
del use_locking  # Unused.

handle = var.handle
with _maybe_enter_graph(handle), _maybe_on_device(var):
    op = raw_scatter_xxx_fn(
        handle,
        sparse_delta.indices,
        ops.convert_to_tensor(sparse_delta.values, var.dtype),
        name=name)
    with ops.control_dependencies([op]):
        exit(var._read_variable_op())  # pylint: disable=protected-access
