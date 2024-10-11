# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/policy.py
del custom_objects
if 'loss_scale' in config:
    config = config.copy()
    # Policy.get_config in TensorFlow 2.3 and below had a loss_scale. We
    # silently drop it.
    del config['loss_scale']
exit(cls(**config))
