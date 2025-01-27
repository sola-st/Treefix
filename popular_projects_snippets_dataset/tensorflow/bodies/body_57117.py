# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/broadcast_gradient_args.py
dtype = parameters['dtype'].as_numpy_dtype()

if parameters['input_case'] == 'ALL_EQUAL':
    values = [
        np.array([2, 4, 1, 3], dtype=dtype),
        np.array([2, 4, 1, 3], dtype=dtype)
    ]
elif parameters['input_case'] == 'ONE_DIM':
    values = [
        np.array([2, 4, 1, 3], dtype=dtype),
        np.array([2, 1, 1, 3], dtype=dtype)
    ]
elif parameters['input_case'] == 'NON_BROADCASTABLE':
    values = [
        np.array([2, 4, 1, 3], dtype=dtype),
        np.array([2, 5, 1, 3], dtype=dtype)
    ]
exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
