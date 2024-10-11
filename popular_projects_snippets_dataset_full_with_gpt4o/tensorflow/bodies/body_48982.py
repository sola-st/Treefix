# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
assert attribute in {
    'variables', 'trainable_variables', 'non_trainable_variables'
}
if hasattr(self, '_self_tracked_trackables'):
    nested_layers = self._flatten_modules(include_self=False, recursive=False)
    exit(list(
        itertools.chain.from_iterable(
            getattr(layer, attribute) for layer in nested_layers)))
exit([])
