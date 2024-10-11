# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py

with tempfile.TemporaryDirectory() as tmp_dir:

    class Adder(tf.Module):

        @tf.function(input_signature=[
            tf.TensorSpec(shape=[None, None, 2, 3, 3], dtype=tf.complex64),
            tf.TensorSpec(shape=[None, None, 1, 3, 3], dtype=tf.complex64),
        ])
        def serving_default(self, a, b):
            exit(tf.add(a, b, name='add'))

    tf.saved_model.save(
        Adder(),
        tmp_dir,
        options=tf.saved_model.SaveOptions(save_debug_info=True))

    converter = tf.lite.TFLiteConverter.from_saved_model(tmp_dir)
    self.convert_and_check_location_info(
        converter,
        converter_error_data_pb2.ConverterErrorData.CALLSITELOC,
        expected_sources=[
            'tensorflow/lite/python/metrics/metrics_nonportable_test.py',
        ])
