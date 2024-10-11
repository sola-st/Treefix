# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/max_pool_with_argmax.py
"""Make a set of tests to do max_pool_with_argmax."""

test_parameters = [{
    'input_size': [[2, 4, 2, 2], [2, 4, 3, 2]],
    'pool_size': [(2, 2), (2, 1)],
    'strides': [(2, 2)],
    'padding': ['SAME', 'VALID'],
}, {
    'input_size': [[2, 4, 10, 2], [2, 4, 11, 2], [2, 4, 12, 2]],
    'pool_size': [(2, 2)],
    'strides': [(2, 3)],
    'padding': ['SAME', 'VALID'],
}]

def build_graph(parameters):
    """Build the exp op testing graph."""
    input_tensor = tf.compat.v1.placeholder(
        dtype=tf.float32, name='input', shape=parameters['input_size'])
    updates, indices = tf.nn.max_pool_with_argmax(
        input_tensor,
        ksize=parameters['pool_size'],
        strides=parameters['strides'],
        padding=parameters['padding'],
        output_dtype=tf.dtypes.int32)
    exit(([input_tensor], [updates, indices]))

def build_inputs(parameters, sess, inputs, outputs):
    values = [
        create_tensor_data(
            tf.float32, parameters['input_size'], min_value=-10, max_value=10)
    ]
    exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))

extra_convert_options = ExtraConvertOptions()
extra_convert_options.allow_custom_ops = True
make_zip_of_tests(options, test_parameters, build_graph, build_inputs,
                  extra_convert_options)
