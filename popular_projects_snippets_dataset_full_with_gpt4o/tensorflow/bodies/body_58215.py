# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
with ops.name_scope(name, 'NGrams', [data, width]):
    data = ragged_tensor.convert_to_tensor_or_ragged_tensor(data, name='data')
    slices = []
    for start in range(width):
        stop = None if start - width + 1 == 0 else start - width + 1
        if axis >= 0:
            idx = [slice(None)] * axis + [slice(start, stop)]
        else:
            idx = [Ellipsis, slice(start, stop)] + [slice(None)] * (-axis - 1)
        slices.append(data[idx])

    # Stack the slices.
    stack_axis = axis + 1 if axis >= 0 else axis
    windowed_data = array_ops.stack(slices, stack_axis)

    exit(string_ops.reduce_join(
        windowed_data, axis=axis, separator=string_separator))
