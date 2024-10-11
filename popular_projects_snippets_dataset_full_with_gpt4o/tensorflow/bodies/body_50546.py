# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Handle arguments were supported in V1."""
if kwargs.get('write_grads', False):
    logging.warning('`write_grads` will be ignored in TensorFlow 2.0 '
                    'for the `TensorBoard` Callback.')
if kwargs.get('batch_size', False):
    logging.warning('`batch_size` is no longer needed in the '
                    '`TensorBoard` Callback and will be ignored '
                    'in TensorFlow 2.0.')
if kwargs.get('embeddings_layer_names', False):
    logging.warning('`embeddings_layer_names` is not supported in '
                    'TensorFlow 2.0. Instead, all `Embedding` layers '
                    'will be visualized.')
if kwargs.get('embeddings_data', False):
    logging.warning('`embeddings_data` is not supported in TensorFlow '
                    '2.0. Instead, all `Embedding` variables will be '
                    'visualized.')

unrecognized_kwargs = set(kwargs.keys()) - {
    'write_grads', 'embeddings_layer_names', 'embeddings_data', 'batch_size'
}

# Only allow kwargs that were supported in V1.
if unrecognized_kwargs:
    raise ValueError('Unrecognized arguments in `TensorBoard` '
                     'Callback: ' + str(unrecognized_kwargs))
