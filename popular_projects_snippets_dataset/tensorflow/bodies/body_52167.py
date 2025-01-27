# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
"""See `input_layer`."""

self._feature_columns = feature_columns
self._weight_collections = weight_collections
self._trainable = trainable
self._cols_to_vars = cols_to_vars
self._name = name
self._input_layer_template = template.make_template(
    self._name, _internal_input_layer, create_scope_now_=create_scope_now)
self._scope = self._input_layer_template.variable_scope
