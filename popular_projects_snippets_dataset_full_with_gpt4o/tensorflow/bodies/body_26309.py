# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/iterator_ops.py
# pylint: disable=protected-access
dataset = dataset._apply_debug_options()

# Store dataset reference to ensure that dataset is alive when this iterator
# is being used. For example, `tf.data.Dataset.from_generator` registers
# a few py_funcs that are needed in `self._next_internal`.  If the dataset
# is deleted, this iterator crashes on `self.__next__(...)` call.
self._dataset = dataset

ds_variant = dataset._variant_tensor
self._element_spec = dataset.element_spec
self._flat_output_types = structure.get_flat_tensor_types(
    self._element_spec)
self._flat_output_shapes = structure.get_flat_tensor_shapes(
    self._element_spec)
with ops.colocate_with(ds_variant):
    self._iterator_resource = (
        gen_dataset_ops.anonymous_iterator_v3(
            output_types=self._flat_output_types,
            output_shapes=self._flat_output_shapes))
    if not context.executing_eagerly():
        # Add full type information to the graph so host memory types inside
        # variants stay on CPU, e.g, ragged string tensors.
        # TODO(b/224776031) Remove this when AnonymousIterateV3 can use
        # (reverse) type inference and all other ops that are needed to
        # provide type information to the AnonymousIterateV3 also support
        # type inference (esp. cross-function type inference) instead of
        # setting the full type information manually.
        fulltype = type_utils.iterator_full_type_from_spec(
            self._element_spec)
        # fulltype is PRODUCT[ITERATOR[PRODUCT[...]]]
        assert len(fulltype.args[0].args[0].args) == len(
            self._flat_output_types)
        self._iterator_resource.op.experimental_set_type(fulltype)
    gen_dataset_ops.make_iterator(ds_variant, self._iterator_resource)
