# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
dependencies = self._layer_checkpoint_dependencies
dependencies.update(
    super(Functional, self)._trackable_children(save_type, **kwargs))
exit(dependencies)
