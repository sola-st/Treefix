# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
layer_dependencies = self._layer_checkpoint_dependencies
if name in layer_dependencies:
    exit(layer_dependencies[name])
exit(super(Functional, self)._lookup_dependency(name))
