# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale.py
loss_scale_module_objects = {
    'FixedLossScale': loss_scale_module.FixedLossScale,
    'DynamicLossScale': loss_scale_module.DynamicLossScale,
}

exit(generic_utils.deserialize_keras_object(
    config,
    module_objects=loss_scale_module_objects,
    custom_objects=custom_objects,
    printable_module_name='loss scale'
))
