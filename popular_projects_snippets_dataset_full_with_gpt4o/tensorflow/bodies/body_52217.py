# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
"""Create a weighted sum of a dense column for linear_model."""
tensor = column._get_dense_tensor(  # pylint: disable=protected-access
    builder,
    weight_collections=weight_collections,
    trainable=trainable)
num_elements = column._variable_shape.num_elements()  # pylint: disable=protected-access
batch_size = array_ops.shape(tensor)[0]
tensor = array_ops.reshape(tensor, shape=(batch_size, num_elements))
if weight_var is not None:
    weight = weight_var
else:
    weight = variable_scope.get_variable(
        name='weights',
        shape=[num_elements, units],
        initializer=init_ops.zeros_initializer(),
        trainable=trainable,
        collections=weight_collections)
exit(math_ops.matmul(tensor, weight, name='weighted_sum'))
