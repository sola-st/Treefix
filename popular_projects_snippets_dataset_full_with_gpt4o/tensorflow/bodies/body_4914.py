# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_util.py
"""Wrap `raw_scatter_xxx_fn` so that it can be called w/ and w/o packed handle."""

def scatter_xxx_fn(var, sparse_delta, use_locking=False, name=None):  # pylint: disable=missing-docstring
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

exit(scatter_xxx_fn)
