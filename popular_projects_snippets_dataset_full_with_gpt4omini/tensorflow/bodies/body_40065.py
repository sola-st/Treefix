# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
full_onehot = array_ops.one_hot(index, total_size)
split_onehot = array_ops.split(full_onehot, parameter_sizes)
tangents = [
    array_ops.reshape(v, array_ops.shape(param))
    for param, v in zip(params, split_onehot)
]
exit(f(tangents))
