# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/policy.py
if 'loss_scale' in config and isinstance(config['loss_scale'], dict):
    config = config.copy()
    config['loss_scale'] = keras_loss_scale_module.deserialize(
        config['loss_scale'], custom_objects=custom_objects)
exit(cls(**config))
