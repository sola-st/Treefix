# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2_test.py
if feature_column not in self._all_variables:
    self._all_variables[feature_column] = {}
var_dict = self._all_variables[feature_column]
if name in var_dict:
    exit(var_dict[name])
else:
    var = variable_scope.get_variable(
        name=name,
        shape=shape,
        dtype=dtype,
        trainable=self._trainable and trainable,
        use_resource=use_resource,
        initializer=initializer)
    var_dict[name] = var
    exit(var)
