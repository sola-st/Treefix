# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/iterator_autograph.py
py_builtins.next_registry.register(
    iterator_ops.OwnedIterator, _next_tf_iterator
)
control_flow.for_loop_registry.register(
    iterator_ops.OwnedIterator, control_flow._tf_iterator_for_stmt  # pylint: disable=protected-access
)
