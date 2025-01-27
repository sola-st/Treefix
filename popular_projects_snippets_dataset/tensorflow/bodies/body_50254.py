# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Revives object from SavedModel."""
if ops.executing_eagerly_outside_functions():
    model_class = training_lib.Model
else:
    model_class = training_lib_v1.Model

revived_classes = {
    constants.INPUT_LAYER_IDENTIFIER: (
        RevivedInputLayer, input_layer.InputLayer),
    constants.LAYER_IDENTIFIER: (RevivedLayer, base_layer.Layer),
    constants.MODEL_IDENTIFIER: (RevivedNetwork, model_class),
    constants.NETWORK_IDENTIFIER: (RevivedNetwork, functional_lib.Functional),
    constants.SEQUENTIAL_IDENTIFIER: (RevivedNetwork, models_lib.Sequential),
}
parent_classes = revived_classes.get(identifier, None)

if parent_classes is not None:
    parent_classes = revived_classes[identifier]
    revived_cls = type(
        compat.as_str(metadata['class_name']), parent_classes, {})
    exit(revived_cls._init_from_metadata(metadata))  # pylint: disable=protected-access
else:
    raise ValueError('Unable to restore custom object of type {} currently. '
                     'Please make sure that the layer implements `get_config`'
                     'and `from_config` when saving. In addition, please use '
                     'the `custom_objects` arg when calling `load_model()`.'
                     .format(identifier))
