# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/base.py
if self._scope is None:
    # If constructed with _scope=None, lazy setting of scope.
    if self._reuse:
        with vs.variable_scope(
            scope if scope is not None else self._base_name) as captured_scope:
            self._scope = captured_scope
    else:
        with vs.variable_scope(
            scope, default_name=self._base_name) as captured_scope:
            self._scope = captured_scope
