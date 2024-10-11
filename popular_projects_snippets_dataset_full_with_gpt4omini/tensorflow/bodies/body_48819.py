# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Loads all layer weights, either from a TensorFlow or an HDF5 weight file.

    If `by_name` is False weights are loaded based on the network's
    topology. This means the architecture should be the same as when the weights
    were saved.  Note that layers that don't have weights are not taken into
    account in the topological ordering, so adding or removing layers is fine as
    long as they don't have weights.

    If `by_name` is True, weights are loaded into layers only if they share the
    same name. This is useful for fine-tuning or transfer-learning models where
    some of the layers have changed.

    Only topological loading (`by_name=False`) is supported when loading weights
    from the TensorFlow format. Note that topological loading differs slightly
    between TensorFlow and HDF5 formats for user-defined classes inheriting from
    `tf.keras.Model`: HDF5 loads based on a flattened list of weights, while the
    TensorFlow format loads based on the object-local names of attributes to
    which layers are assigned in the `Model`'s constructor.

    Args:
        filepath: String, path to the weights file to load. For weight files in
            TensorFlow format, this is the file prefix (the same as was passed
            to `save_weights`). This can also be a path to a SavedModel
            saved from `model.save`.
        by_name: Boolean, whether to load weights by name or by topological
            order. Only topological loading is supported for weight files in
            TensorFlow format.
        skip_mismatch: Boolean, whether to skip loading of layers where there is
            a mismatch in the number of weights, or a mismatch in the shape of
            the weight (only valid when `by_name=True`).
        options: Optional `tf.train.CheckpointOptions` object that specifies
            options for loading weights.

    Returns:
        When loading a weight file in TensorFlow format, returns the same status
        object as `tf.train.Checkpoint.restore`. When graph building, restore
        ops are run automatically as soon as the network is built (on first call
        for user-defined classes inheriting from `Model`, immediately if it is
        already built).

        When loading weights in HDF5 format, returns `None`.

    Raises:
        ImportError: If h5py is not available and the weight file is in HDF5
            format.
        ValueError: If `skip_mismatch` is set to `True` when `by_name` is
          `False`.
    """
if backend.is_tpu_strategy(self._distribution_strategy):
    if (self._distribution_strategy.extended.steps_per_run > 1 and
        (not saving_utils.is_hdf5_filepath(filepath))):
        raise ValueError('Load weights is not yet supported with TPUStrategy '
                         'with steps_per_run greater than 1.')
if skip_mismatch and not by_name:
    raise ValueError(
        'When calling model.load_weights, skip_mismatch can only be set to '
        'True when by_name is True.')

filepath, save_format = _detect_save_format(filepath)
if save_format == 'tf':
    status = self._checkpoint.read(filepath, options)
    if by_name:
        raise NotImplementedError(
            'Weights may only be loaded based on topology into Models when '
            'loading TensorFlow-formatted weights (got by_name=True to '
            'load_weights).')
    if not context.executing_eagerly():
        session = backend.get_session()
        # Restore existing variables (if any) immediately, and set up a
        # streaming restore for any variables created in the future.
        trackable_utils.streaming_restore(status=status, session=session)
    status.assert_nontrivial_match()
else:
    status = None
    if h5py is None:
        raise ImportError(
            '`load_weights` requires h5py when loading weights from HDF5.')
    if not self._is_graph_network and not self.built:
        raise ValueError(
            'Unable to load weights saved in HDF5 format into a subclassed '
            'Model which has not created its variables yet. Call the Model '
            'first, then load the weights.')
    self._assert_weights_created()
    with h5py.File(filepath, 'r') as f:
        if 'layer_names' not in f.attrs and 'model_weights' in f:
            f = f['model_weights']
        if by_name:
            hdf5_format.load_weights_from_hdf5_group_by_name(
                f, self.layers, skip_mismatch=skip_mismatch)
        else:
            hdf5_format.load_weights_from_hdf5_group(f, self.layers)

    # Perform any layer defined finalization of the layer state.
for layer in self.layers:
    layer.finalize_state()
exit(status)
