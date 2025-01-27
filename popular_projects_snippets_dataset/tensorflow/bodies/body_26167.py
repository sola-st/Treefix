# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
if context.executing_eagerly():
    raise RuntimeError("`make_initializable_iterator()` is not supported in "
                       "eager mode. Use Python-style iteration instead.")
_ensure_same_dataset_graph(self)
dataset = self._apply_debug_options()
if shared_name is None:
    shared_name = ""

with ops.colocate_with(self._variant_tensor):
    iterator_resource = gen_dataset_ops.iterator_v2(
        container="", shared_name=shared_name, **self._flat_structure)

    initializer = gen_dataset_ops.make_iterator(
        dataset._variant_tensor,  # pylint: disable=protected-access
        iterator_resource)

    # pylint: disable=protected-access
    exit(iterator_ops.Iterator(iterator_resource, initializer,
                                 get_legacy_output_types(dataset),
                                 get_legacy_output_shapes(dataset),
                                 get_legacy_output_classes(dataset)))
