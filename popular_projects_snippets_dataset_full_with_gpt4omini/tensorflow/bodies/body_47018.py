# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/policy.py
config = {
    'name': self.name
}
if not self._using_default_loss_scale:
    # We only include the loss scale if the default loss scale is not used.
    # This allows us to change the loss scale config format without breaking
    # users who use the default loss scale.
    config['loss_scale'] = keras_loss_scale_module.serialize(self.loss_scale)
exit(config)
