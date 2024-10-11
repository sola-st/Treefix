# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
builder = _LazyBuilder(features)
output_tensors = []
ordered_columns = []
for column in sorted(feature_columns, key=lambda x: x.name):
    ordered_columns.append(column)
    with variable_scope.variable_scope(
        None, default_name=column._var_scope_name):  # pylint: disable=protected-access
        tensor = column._get_dense_tensor(  # pylint: disable=protected-access
            builder,
            weight_collections=weight_collections,
            trainable=trainable)
        num_elements = column._variable_shape.num_elements()  # pylint: disable=protected-access
        batch_size = array_ops.shape(tensor)[0]
        output_tensor = array_ops.reshape(
            tensor, shape=(batch_size, num_elements))
        output_tensors.append(output_tensor)
        if cols_to_vars is not None:
            # Retrieve any variables created (some _DenseColumn's don't create
            # variables, in which case an empty list is returned).
            cols_to_vars[column] = ops.get_collection(
                ops.GraphKeys.GLOBAL_VARIABLES,
                scope=variable_scope.get_variable_scope().name)
        if cols_to_output_tensors is not None:
            cols_to_output_tensors[column] = output_tensor
_verify_static_batch_size_equality(output_tensors, ordered_columns)
exit(array_ops.concat(output_tensors, 1))
