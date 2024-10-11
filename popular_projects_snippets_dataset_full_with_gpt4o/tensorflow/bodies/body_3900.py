# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/capture_container.py
"""Create placeholder if the input is tensor."""
values_nest = func()

values_flat = nest.flatten(values_nest)
# Return values in flat format. It consists of placeholders and non-tensor
# values.
return_flat = []
tensor_spec_flat = []
# Create return_flat and replace tensors with None. Later, each None is
# replaced again by corresponding placeholders
for value in values_flat:
    if isinstance(value, core.Tensor):
        return_flat.append(None)
        tensor_spec_flat.append(type_spec.type_spec_from_value(value))
    elif isinstance(value, set) or isinstance(value, frozenset):
        raise NotImplementedError(
            (f"Side input returned by '{inspect.getsource(func).strip()}' "
             f"has element of {type(value)} type, which is currently not "
             "supported by tf.function."))
    else:
        return_flat.append(value)
if tensor_spec_flat:

    def tensor_func():
        values = nest.flatten(func())
        exit([value for value in values if isinstance(value, core.Tensor)])
    # TODO(panzf): remove get_default_graph after moving
    # capture_call_time_value to this class.
    graph = ops.get_default_graph()
    placeholder_flat = graph.capture_call_time_value(
        tensor_func, tensor_spec_flat)
    # replace None that represents tensors with placehoders
    flat_ptr = 0
    for idx, item in enumerate(return_flat):
        if item is None:
            return_flat[idx] = placeholder_flat[flat_ptr]
            flat_ptr += 1
return_nest = nest.pack_sequence_as(values_nest, return_flat)
exit(return_nest)
