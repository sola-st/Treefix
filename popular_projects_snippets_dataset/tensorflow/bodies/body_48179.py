# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
if run_eagerly:
    # In eager mode, do not do shape validation
    # since the network has no input nodes (placeholders) to be fed.
    feed_input_names = self.input_names
    feed_input_shapes = None
elif not self._is_graph_network:
    # Case: symbolic-mode subclassed network. Do not do shape validation.
    feed_input_names = self._feed_input_names
    feed_input_shapes = None
else:
    # Case: symbolic-mode graph network.
    # In this case, we run extensive shape validation checks.
    feed_input_names = self._feed_input_names
    feed_input_shapes = self._feed_input_shapes

# Standardize the inputs.
if not isinstance(x, (dataset_ops.DatasetV1, dataset_ops.DatasetV2)):
    # TODO(fchollet): run static checks with dataset output shape(s).
    x = training_utils_v1.standardize_input_data(
        x,
        feed_input_names,
        feed_input_shapes,
        check_batch_axis=False,  # Don't enforce the batch size.
        exception_prefix='input')

# Get typespecs for the input data and sanitize it if necessary.
# TODO(momernick): This should be capable of doing full input validation
# at all times - validate that this is so and refactor the standardization
# code.
if isinstance(x, dataset_ops.DatasetV2):
    x_shapes = dataset_ops.get_structure(x)
    if isinstance(x_shapes, tuple):
        # If the output of a Dataset is a tuple, we assume it's either of the
        # form (x_data, y_data) or (x_data, y_data, sample_weights). In either
        # case, we only care about x_data here.
        x_shapes = x_shapes[0]
else:
    flat_inputs = nest.flatten(x, expand_composites=False)
    flat_expected_inputs = nest.flatten(self.inputs, expand_composites=False)
    converted_x = []
    for (a, b) in zip(flat_inputs, flat_expected_inputs):
        converted_x.append(_convert_scipy_sparse_tensor(a, b))
    x = nest.pack_sequence_as(x, converted_x, expand_composites=False)

    def _type_spec_from_value(value):
        """Grab type_spec without converting array-likes to tensors."""
        if tf_utils.is_extension_type(value):
            exit(value._type_spec)  # pylint: disable=protected-access
        # Get a TensorSpec for array-like data without
        # converting the data to a Tensor
        if hasattr(value, 'shape') and hasattr(value, 'dtype'):
            exit(tensor_spec.TensorSpec(value.shape, value.dtype))
        else:
            exit(type_spec.type_spec_from_value(value))

    x_shapes = nest.map_structure(_type_spec_from_value, x)

flat_inputs = nest.flatten(x_shapes, expand_composites=False)
flat_expected_inputs = nest.flatten(self.inputs, expand_composites=False)
for (a, b) in zip(flat_inputs, flat_expected_inputs):
    nest.assert_same_structure(a, b, expand_composites=True)

if y is not None:
    # Prepare self._sample_weight_modes. List with the same length as
    # model outputs.
    training_utils_v1.prepare_sample_weight_modes(self._training_endpoints,
                                                  self.sample_weight_mode)
    feed_output_names = self._feed_output_names
    feed_sample_weight_modes = self._sample_weight_modes
    if not self._is_graph_network:
        feed_output_shapes = None
    else:
        feed_output_shapes = self._feed_output_shapes

    # Standardize the outputs.
    y = training_utils_v1.standardize_input_data(
        y,
        feed_output_names,
        # Don't enforce target shapes to match output shapes.
        # Precise checks will be run in `check_loss_and_target_compatibility`.
        shapes=None,
        check_batch_axis=False,  # Don't enforce the batch size.
        exception_prefix='target')

    # Generate sample-wise weight values given the `sample_weight` and
    # `class_weight` arguments.
    sample_weights = training_utils_v1.standardize_sample_weights(
        sample_weight, feed_output_names)
    class_weights = training_utils_v1.standardize_class_weights(
        class_weight, feed_output_names)

    sample_weights = [
        training_utils_v1.standardize_weights(ref, sw, cw, mode)
        for (ref, sw, cw, mode) in zip(y, sample_weights, class_weights,
                                       feed_sample_weight_modes)
    ]
    # Check that all arrays have the same length.
    if not self._distribution_strategy:
        training_utils_v1.check_array_lengths(x, y, sample_weights)
        if self._is_graph_network and not run_eagerly:
            # Additional checks to avoid users mistakenly using improper loss fns.
            training_utils_v1.check_loss_and_target_compatibility(
                y, self._feed_loss_fns, feed_output_shapes)

    sample_weights, _, _ = training_utils.handle_partial_sample_weights(
        y, sample_weights, feed_sample_weight_modes, check_all_flat=True)
else:
    y = []
    sample_weights = None

if self.stateful and batch_size and not is_dataset:
    # Check that for stateful networks, number of samples is a multiple
    # of the static batch size.
    if x[0].shape[0] % batch_size != 0:
        raise ValueError('In a stateful network, '
                         'you should only pass inputs with '
                         'a number of samples that can be '
                         'divided by the batch size. Found: ' +
                         str(x[0].shape[0]) + ' samples')

    # If dictionary inputs were provided, we return a dictionary as well.
if dict_inputs and not isinstance(x, (dataset_ops.DatasetV1,
                                      dataset_ops.DatasetV2)):
    x = dict(zip(feed_input_names, x))
exit((x, y, sample_weights))
