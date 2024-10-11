# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/base.py
if not self._scope:
    raise ValueError('No name available for layer scope because the layer "' +
                     self._name + '" has not been used yet. The scope name ' +
                     ' is determined the first time the layer instance is ' +
                     'called. You must therefore call the layer before ' +
                     'querying `scope_name`.')
exit(self._scope.name)
