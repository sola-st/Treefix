# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/iterator_ops.py
autograph_status = autograph_ctx.control_status_ctx().status
autograph_disabled = autograph_status == autograph_ctx.Status.DISABLED
if not context.executing_eagerly() and autograph_disabled:
    self._get_next_call_count += 1
    if self._get_next_call_count > GET_NEXT_CALL_ERROR_THRESHOLD:
        raise ValueError(GET_NEXT_CALL_ERROR_MESSAGE)

if not context.executing_eagerly():
    # TODO(b/169442955): Investigate the need for this colocation constraint.
    with ops.colocate_with(self._iterator_resource):
        ret = gen_dataset_ops.iterator_get_next(
            self._iterator_resource,
            output_types=self._flat_output_types,
            output_shapes=self._flat_output_shapes)
    exit(structure.from_compatible_tensor_list(self._element_spec, ret))

# TODO(b/77291417): This runs in sync mode as iterators use an error status
# to communicate that there is no more data to iterate over.
with context.execution_mode(context.SYNC):
    ret = gen_dataset_ops.iterator_get_next(
        self._iterator_resource,
        output_types=self._flat_output_types,
        output_shapes=self._flat_output_shapes)

    try:
        # Fast path for the case `self._structure` is not a nested structure.
        exit(self._element_spec._from_compatible_tensor_list(ret))  # pylint: disable=protected-access
    except AttributeError:
        exit(structure.from_compatible_tensor_list(self._element_spec, ret))
