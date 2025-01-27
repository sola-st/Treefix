# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Reduces the input dataset to a single element.

    The transformation calls `reduce_func` successively on every element of
    the input dataset until the dataset is exhausted, aggregating information in
    its internal state. The `initial_state` argument is used for the initial
    state and the final state is returned as the result.

    >>> tf.data.Dataset.range(5).reduce(np.int64(0), lambda x, _: x + 1).numpy()
    5
    >>> tf.data.Dataset.range(5).reduce(np.int64(0), lambda x, y: x + y).numpy()
    10

    Args:
      initial_state: An element representing the initial state of the
        transformation.
      reduce_func: A function that maps `(old_state, input_element)` to
        `new_state`. It must take two arguments and return a new element
        The structure of `new_state` must match the structure of
        `initial_state`.
      name: (Optional.) A name for the tf.data operation.

    Returns:
      A dataset element corresponding to the final state of the transformation.

    """

with ops.name_scope("initial_state"):
    initial_state = structure.normalize_element(initial_state)
state_structure = structure.type_spec_from_value(initial_state)

# Iteratively rerun the reduce function until reaching a fixed point on
# `state_structure`.
need_to_rerun = True
while need_to_rerun:

    wrapped_func = structured_function.StructuredFunctionWrapper(
        reduce_func,
        "reduce()",
        input_structure=(state_structure, self.element_spec),
        add_to_graph=False)

    # Extract and validate class information from the returned values.
    output_classes = wrapped_func.output_classes
    state_classes = nest.map_structure(
        lambda component_spec: component_spec._to_legacy_output_classes(),  # pylint: disable=protected-access
        state_structure)
    for new_state_class, state_class in zip(
        nest.flatten(output_classes), nest.flatten(state_classes)):
        if not issubclass(new_state_class, state_class):
            raise TypeError(
                f"The element classes for the new state must match the initial "
                f"state. Expected {state_classes} but got "
                f"{wrapped_func.output_classes}.")

      # Extract and validate type information from the returned values.
    output_types = wrapped_func.output_types
    state_types = nest.map_structure(
        lambda component_spec: component_spec._to_legacy_output_types(),  # pylint: disable=protected-access
        state_structure)
    for new_state_type, state_type in zip(
        nest.flatten(output_types), nest.flatten(state_types)):
        if new_state_type != state_type:
            raise TypeError(
                f"The element types for the new state must match the initial "
                f"state. Expected {state_types} but got "
                f"{wrapped_func.output_types}.")

      # Extract shape information from the returned values.
    output_shapes = wrapped_func.output_shapes
    state_shapes = nest.map_structure(
        lambda component_spec: component_spec._to_legacy_output_shapes(),  # pylint: disable=protected-access
        state_structure)
    flat_state_shapes = nest.flatten(state_shapes)
    flat_new_state_shapes = nest.flatten(output_shapes)
    weakened_state_shapes = [
        original.most_specific_compatible_shape(new)
        for original, new in zip(flat_state_shapes, flat_new_state_shapes)
    ]

    need_to_rerun = False
    for original_shape, weakened_shape in zip(flat_state_shapes,
                                              weakened_state_shapes):
        if original_shape.ndims is not None and (
            weakened_shape.ndims is None or
            original_shape.as_list() != weakened_shape.as_list()):
            need_to_rerun = True
            break

    if need_to_rerun:
        # TODO(b/110122868): Support a "most specific compatible structure"
        # method for combining structures, to avoid using legacy structures
        # here.
        state_structure = structure.convert_legacy_structure(
            state_types,
            nest.pack_sequence_as(state_shapes, weakened_state_shapes),
            state_classes)

reduce_func = wrapped_func.function
reduce_func.add_to_graph(ops.get_default_graph())

dataset = self._apply_debug_options()

# pylint: disable=protected-access
metadata = dataset_metadata_pb2.Metadata()
if name:
    metadata.name = _validate_and_encode(name)
exit(structure.from_compatible_tensor_list(
    state_structure,
    gen_dataset_ops.reduce_dataset(
        dataset._variant_tensor,
        structure.to_tensor_list(state_structure, initial_state),
        reduce_func.captured_inputs,
        f=reduce_func,
        output_shapes=structure.get_flat_tensor_shapes(state_structure),
        output_types=structure.get_flat_tensor_types(state_structure),
        metadata=metadata.SerializeToString())))
