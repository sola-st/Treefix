# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks_v1.py
"""Sets Keras model and creates summary ops."""

self.model = model
self._init_writer(model)
# histogram summaries only enabled in graph mode
if not context.executing_eagerly():
    self._make_histogram_ops(model)
    self.merged = tf_summary.merge_all()

# If both embedding_freq and embeddings_data are available, we will
# visualize embeddings.
if self.embeddings_freq and self.embeddings_data is not None:
    # Avoid circular dependency.
    from tensorflow.python.keras.engine import training_utils_v1  # pylint: disable=g-import-not-at-top
    self.embeddings_data = training_utils_v1.standardize_input_data(
        self.embeddings_data, model.input_names)

    # If embedding_layer_names are not provided, get all of the embedding
    # layers from the model.
    embeddings_layer_names = self.embeddings_layer_names
    if not embeddings_layer_names:
        embeddings_layer_names = [
            layer.name
            for layer in self.model.layers
            if type(layer).__name__ == 'Embedding'
        ]

    self.assign_embeddings = []
    embeddings_vars = {}

    self.batch_id = batch_id = array_ops.placeholder(dtypes.int32)
    self.step = step = array_ops.placeholder(dtypes.int32)

    for layer in self.model.layers:
        if layer.name in embeddings_layer_names:
            embedding_input = self.model.get_layer(layer.name).output
            embedding_size = np.prod(embedding_input.shape[1:])
            embedding_input = array_ops.reshape(embedding_input,
                                                (step, int(embedding_size)))
            shape = (self.embeddings_data[0].shape[0], int(embedding_size))
            embedding = variables.Variable(
                array_ops.zeros(shape), name=layer.name + '_embedding')
            embeddings_vars[layer.name] = embedding
            batch = state_ops.assign(embedding[batch_id:batch_id + step],
                                     embedding_input)
            self.assign_embeddings.append(batch)

    self.saver = saver.Saver(list(embeddings_vars.values()))

    # Create embeddings_metadata dictionary
    if isinstance(self.embeddings_metadata, str):
        embeddings_metadata = {
            layer_name: self.embeddings_metadata
            for layer_name in embeddings_vars.keys()
        }
    else:
        # If embedding_metadata is already a dictionary
        embeddings_metadata = self.embeddings_metadata

    try:
        from tensorboard.plugins import projector
    except ImportError:
        raise ImportError('Failed to import TensorBoard. Please make sure that '
                          'TensorBoard integration is complete."')

    # TODO(psv): Add integration tests to test embedding visualization
    # with TensorBoard callback. We are unable to write a unit test for this
    # because TensorBoard dependency assumes TensorFlow package is installed.
    config = projector.ProjectorConfig()
    for layer_name, tensor in embeddings_vars.items():
        embedding = config.embeddings.add()
        embedding.tensor_name = tensor.name

        if (embeddings_metadata is not None and
            layer_name in embeddings_metadata):
            embedding.metadata_path = embeddings_metadata[layer_name]

    projector.visualize_embeddings(self.writer, config)
