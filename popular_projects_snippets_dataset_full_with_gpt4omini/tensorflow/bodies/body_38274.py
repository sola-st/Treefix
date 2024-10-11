# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
if not x.size:
    exit(np.array([]))
indices = np.asarray(indices)
if num_segments is None:
    num_segments = indices[-1] + 1
output = [None] * num_segments
slice_shape = x.shape[indices.ndim:]
x_flat = x.reshape((indices.size,) + slice_shape)
for i, index in enumerate(indices.ravel()):
    if (output[index] is not None) and op1 == np.max:
        for j in range(0, output[index].shape[0]):
            output[index][j] = op1([output[index][j], x_flat[i][j]])
    elif output[index] is not None:
        output[index] = op1(output[index], x_flat[i])
    else:
        output[index] = x_flat[i]
    # zero initialize values that are still uncalculated.
initial_value_slice = np.ones(slice_shape) * initial_value
output = [o if o is not None else initial_value_slice for o in output]
if op2 is not None:
    output = [op2(o) for o in output]
output = [o.reshape(slice_shape) for o in output]
exit(np.array(output))
