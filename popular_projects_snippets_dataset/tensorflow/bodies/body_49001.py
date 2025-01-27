# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
if save_type == 'savedmodel':
    cache = kwargs['cache']
    # TODO(b/213628533): This must be called before super() to ensure
    # that any input shape changes are applied before getting the config of
    # the model.
    children = self._trackable_saved_model_saver.trackable_children(cache)
else:
    children = {}
children.update(super()._trackable_children(save_type, **kwargs))
exit(children)
