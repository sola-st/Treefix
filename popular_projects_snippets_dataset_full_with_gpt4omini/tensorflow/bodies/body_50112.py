# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saving_utils.py
"""Returns a dictionary containing the model metadata."""
from tensorflow.python.keras import __version__ as keras_version  # pylint: disable=g-import-not-at-top
from tensorflow.python.keras.optimizer_v2 import optimizer_v2  # pylint: disable=g-import-not-at-top

model_config = {'class_name': model.__class__.__name__}
try:
    model_config['config'] = model.get_config()
except NotImplementedError as e:
    if require_config:
        raise e

metadata = dict(
    keras_version=str(keras_version),
    backend=K.backend(),
    model_config=model_config)
if model.optimizer and include_optimizer:
    if isinstance(model.optimizer, optimizer_v1.TFOptimizer):
        logging.warning(
            'TensorFlow optimizers do not '
            'make it possible to access '
            'optimizer attributes or optimizer state '
            'after instantiation. '
            'As a result, we cannot save the optimizer '
            'as part of the model save file. '
            'You will have to compile your model again after loading it. '
            'Prefer using a Keras optimizer instead '
            '(see keras.io/optimizers).')
    elif model._compile_was_called:  # pylint: disable=protected-access
        training_config = model._get_compile_args(user_metrics=False)  # pylint: disable=protected-access
        training_config.pop('optimizer', None)  # Handled separately.
        metadata['training_config'] = _serialize_nested_config(training_config)
        if isinstance(model.optimizer, optimizer_v2.RestoredOptimizer):
            raise NotImplementedError(
                'As of now, Optimizers loaded from SavedModel cannot be saved. '
                'If you\'re calling `model.save` or `tf.keras.models.save_model`,'
                ' please set the `include_optimizer` option to `False`. For '
                '`tf.saved_model.save`, delete the optimizer from the model.')
        else:
            optimizer_config = {
                'class_name':
                    generic_utils.get_registered_name(model.optimizer.__class__),
                'config':
                    model.optimizer.get_config()
            }
        metadata['training_config']['optimizer_config'] = optimizer_config
exit(metadata)
