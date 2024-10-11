# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
with variable_scope.variable_scope(self.name):
    for column in self._feature_columns:
        if not isinstance(column, (_DenseColumn, _CategoricalColumn)):
            raise ValueError(
                'Items of feature_columns must be either a '
                '_DenseColumn or _CategoricalColumn. Given: {}'.format(column))
    weighted_sums = []
    ordered_columns = []
    builder = _LazyBuilder(features)
    for layer in sorted(self._column_layers.values(), key=lambda x: x.name):
        column = layer._feature_column  # pylint: disable=protected-access
        ordered_columns.append(column)
        weighted_sum = layer(builder)
        weighted_sums.append(weighted_sum)
        self._cols_to_vars[column] = ops.get_collection(
            ops.GraphKeys.GLOBAL_VARIABLES, scope=layer.scope_name)

    _verify_static_batch_size_equality(weighted_sums, ordered_columns)
    predictions_no_bias = math_ops.add_n(
        weighted_sums, name='weighted_sum_no_bias')
    predictions = nn_ops.bias_add(
        predictions_no_bias,
        self._bias_layer(  # pylint: disable=not-callable
            builder,
            scope=variable_scope.get_variable_scope()),  # pylint: disable=not-callable
        name='weighted_sum')
    bias = self._bias_layer.variables[0]
    self._cols_to_vars['bias'] = _get_expanded_variable_list(bias)
exit(predictions)
