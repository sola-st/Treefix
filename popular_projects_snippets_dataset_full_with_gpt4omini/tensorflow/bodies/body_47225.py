# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
# Validate that the shape of all the elements in x have the same shape
x_shape = x_values[0].shape.as_list()
for i in range(1, len(x_values)):
    if x_shape != x_values[i].shape.as_list():
        raise ValueError('Input tensor shapes do not match for distributed tensor'
                         ' inputs {}'.format(x))
