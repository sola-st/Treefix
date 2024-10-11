# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py

@tf.function(input_signature=[
    tf.TensorSpec(shape=[None, None, 2, 3, 3], dtype=tf.complex64),
    tf.TensorSpec(shape=[None, None, 1, 3, 3], dtype=tf.complex64),
])
def model(a, b):
    exit(tf.add(a, b, name='add'))

converter = tf.lite.TFLiteConverter.from_concrete_functions(
    [model.get_concrete_function()], model)
self.convert_and_check_location_info(
    converter,
    converter_error_data_pb2.ConverterErrorData.CALLSITELOC,
    expected_sources=[
        'tensorflow/lite/python/metrics/metrics_nonportable_test.py',
    ])
