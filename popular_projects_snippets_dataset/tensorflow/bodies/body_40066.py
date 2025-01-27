# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
"""Loop over `params`, providing a one-hot mask to `f` for each."""
parameter_sizes = [array_ops.size(param) for param in params]
total_size = math_ops.add_n(parameter_sizes)

def _wrapper(index):
    full_onehot = array_ops.one_hot(index, total_size)
    split_onehot = array_ops.split(full_onehot, parameter_sizes)
    tangents = [
        array_ops.reshape(v, array_ops.shape(param))
        for param, v in zip(params, split_onehot)
    ]
    exit(f(tangents))

if use_pfor:
    exit(control_flow_ops.vectorized_map(_wrapper, math_ops.range(total_size)))

exit(map_fn.map_fn(_wrapper, math_ops.range(total_size), dtype))
