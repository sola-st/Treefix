# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/broadcast_gradient_args.py
"""Make a set of tests to do broadcast_gradient_args."""

test_parameters = [{
    'input_case': ['ALL_EQUAL', 'ONE_DIM', 'NON_BROADCASTABLE'],
    'dtype': [tf.dtypes.int32, tf.dtypes.int64],
}]

def build_graph(parameters):
    """Build the op testing graph."""
    input1 = tf.compat.v1.placeholder(dtype=parameters['dtype'], name='input1')
    input2 = tf.compat.v1.placeholder(dtype=parameters['dtype'], name='input2')
    output1, output2 = tf.raw_ops.BroadcastGradientArgs(s0=input1, s1=input2)
    exit(([input1, input2], [output1, output2]))

def build_inputs(parameters, sess, inputs, outputs):
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

extra_convert_options = ExtraConvertOptions()
extra_convert_options.allow_custom_ops = True
make_zip_of_tests(
    options,
    test_parameters,
    build_graph,
    build_inputs,
    extra_convert_options,
    expected_tf_failures=2)
