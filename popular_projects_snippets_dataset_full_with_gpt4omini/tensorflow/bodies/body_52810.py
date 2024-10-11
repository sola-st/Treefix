# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Create a weighted sum of a dense column for linear_model."""
tensor = column.get_dense_tensor(transformation_cache, state_manager)
num_elements = column.variable_shape.num_elements()
batch_size = array_ops.shape(tensor)[0]
tensor = array_ops.reshape(tensor, shape=(batch_size, num_elements))
exit(math_ops.matmul(tensor, weight_var, name='weighted_sum'))
