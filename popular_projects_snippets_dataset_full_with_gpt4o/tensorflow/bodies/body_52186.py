# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
super(_LinearModel, self).__init__(name=name, **kwargs)
# We force the keras_style to be True here, as a workaround to not being
# able to inherit keras.layers.Layer as base class. Setting this will let
# us skip all the legacy behavior for base.Layer.
# Also note that we use Layer as base class, instead of Model, since there
# isn't any Model specific behavior gets used, eg compile/fit.
self._keras_style = True
self._feature_columns = _normalize_feature_columns(feature_columns)
self._weight_collections = list(weight_collections or [])
if ops.GraphKeys.GLOBAL_VARIABLES not in self._weight_collections:
    self._weight_collections.append(ops.GraphKeys.GLOBAL_VARIABLES)
if ops.GraphKeys.MODEL_VARIABLES not in self._weight_collections:
    self._weight_collections.append(ops.GraphKeys.MODEL_VARIABLES)

column_layers = {}
for column in sorted(self._feature_columns, key=lambda x: x.name):
    with variable_scope.variable_scope(
        None, default_name=column._var_scope_name) as vs:  # pylint: disable=protected-access
        # Having the fully expressed variable scope name ends up doubly
        # expressing the outer scope (scope with which this method was called)
        # in the name of the variable that would get created.
        column_name = _strip_leading_slashes(vs.name)
    column_layer = _FCLinearWrapper(column, units, sparse_combiner,
                                    self._weight_collections, trainable,
                                    column_name, **kwargs)
    column_layers[column_name] = column_layer
self._column_layers = self._add_layers(column_layers)
self._bias_layer = _BiasLayer(
    units=units,
    trainable=trainable,
    weight_collections=self._weight_collections,
    name='bias_layer',
    **kwargs)
self._cols_to_vars = {}
