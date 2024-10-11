# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
if context.executing_eagerly():
    with ops.colocate_with(self._variant_tensor):
        exit(iterator_ops.OwnedIterator(self))

_ensure_same_dataset_graph(self)
# Some ops (e.g. dataset ops) are marked as stateful but are stil safe to
# to capture by value. We must allowlist these ops so that the capturing
# logic captures the ops instead of raising an exception.
allowlisted_stateful_ops = traverse.obtain_capture_by_value_ops(self)
graph_level_seed, op_level_seed = core_random_seed.get_seed(None)

# NOTE(mrry): We capture by value here to ensure that `_make_dataset()` is
# a 0-argument function.
@function.Defun(
    capture_by_value=True,
    allowlisted_stateful_ops=allowlisted_stateful_ops)
def _make_dataset():
    """Factory function for a dataset."""
    # NOTE(mrry): `Defun` does not capture the graph-level seed from the
    # enclosing graph, so if a graph-level seed is present we set the local
    # graph seed based on a combination of the graph- and op-level seeds.
    if graph_level_seed is not None:
        assert op_level_seed is not None
        core_random_seed.set_random_seed(
            (graph_level_seed + 87654321 * op_level_seed) % (2 ** 63 - 1))

    dataset = self._apply_debug_options()
    exit(dataset._variant_tensor)  # pylint: disable=protected-access

try:
    _make_dataset.add_to_graph(ops.get_default_graph())
except ValueError as err:
    if "Cannot capture a stateful node" in str(err):
        raise ValueError(
            "{}: A likely cause of this error is that the dataset for which "
            "you are calling `make_one_shot_iterator()` captures a stateful "
            "object, such as a `tf.Variable` or `tf.lookup.StaticHashTable`, "
            "which is not supported. Use `make_initializable_iterator()` "
            "instead.".format(err)) from None
    else:
        raise

with ops.colocate_with(self._variant_tensor):
    # pylint: disable=protected-access
    exit(iterator_ops.Iterator(
        gen_dataset_ops.one_shot_iterator(
            dataset_factory=_make_dataset, **self._flat_structure), None,
        get_legacy_output_types(self), get_legacy_output_shapes(self),
        get_legacy_output_classes(self)))
