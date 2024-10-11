# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
x_dtype = x_values[0].dtype
for i in range(1, len(x_values)):
    if x_dtype != x_values[i].dtype:
        raise ValueError('Input tensor dtypes do not match for distributed tensor'
                         ' inputs {}'.format(x))
