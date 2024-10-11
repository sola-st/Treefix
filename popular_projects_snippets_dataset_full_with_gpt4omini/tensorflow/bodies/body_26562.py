# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/grouping.py
"""Make wrapping defun for reduce_func."""

# Iteratively rerun the reduce function until reaching a fixed point on
# `self._state_structure`.
self._state_structure = self._init_func.output_structure
state_types = self._init_func.output_types
state_shapes = self._init_func.output_shapes
state_classes = self._init_func.output_classes
need_to_rerun = True
while need_to_rerun:

    wrapped_func = structured_function.StructuredFunctionWrapper(
        reduce_func,
        self._transformation_name(),
        input_structure=(self._state_structure, input_dataset.element_spec),
        add_to_graph=False)

    # Extract and validate class information from the returned values.
    for new_state_class, state_class in zip(
        nest.flatten(wrapped_func.output_classes),
        nest.flatten(state_classes)):
        if not issubclass(new_state_class, state_class):
            raise TypeError(
                f"Invalid `reducer`. The output class of the "
                f"`reducer.reduce_func` {wrapped_func.output_classes}, "
                f"does not match the class of the reduce state "
                f"{self._state_classes}.")

      # Extract and validate type information from the returned values.
    for new_state_type, state_type in zip(
        nest.flatten(wrapped_func.output_types), nest.flatten(state_types)):
        if new_state_type != state_type:
            raise TypeError(
                f"Invalid `reducer`. The element types for the new state "
                f"{wrapped_func.output_types} do not match the element types "
                f"of the old state {self._init_func.output_types}."
            )

      # Extract shape information from the returned values.
    flat_state_shapes = nest.flatten(state_shapes)
    flat_new_state_shapes = nest.flatten(wrapped_func.output_shapes)
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
        state_shapes = nest.pack_sequence_as(
            self._init_func.output_shapes, weakened_state_shapes)
        self._state_structure = structure.convert_legacy_structure(
            state_types, state_shapes, state_classes)

self._reduce_func = wrapped_func
self._reduce_func.function.add_to_graph(ops.get_default_graph())
