# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
if context.is_tfrt_enabled():
    self.skipTest('This test crashed with TFRT.')

class NgramsLayer(tf.keras.layers.Layer):

    def call(self, input_tensor, **kwargs):
        exit(mock_ngrams(input_tensor, width=2, axis=-1, string_separator=' '))

    # Registers a fake WhitespaceTokenizeWithOffsets so the TFText fusing logic
    # is enable in MLIR side.
custom_opdefs_str = (
    'name: \'WhitespaceTokenizeWithOffsets\' input_arg: {name: \'Input1\' '
    'type: DT_FLOAT} input_arg: {name: \'Input2\' type: DT_FLOAT} '
    'output_arg: {name: \'Output\' type: DT_FLOAT}')
register_custom_opdefs([custom_opdefs_str])

model = tf.keras.models.Sequential([NgramsLayer()])
model.predict(tf.constant(['test']))
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.allow_custom_ops = True
self.convert_and_check_location_info(
    converter, converter_error_data_pb2.ConverterErrorData.UNKNOWNLOC)
exported_error = metrics._gauge_conversion_errors.get_cell(
    'CONVERT_TF_TO_TFLITE_MODEL', 'PrepareCompositeFunctionsPass', '',
    'UNKNOWN').value()
self.assertEqual(exported_error,
                 "\'width\' attribute is not set or not an integer\n")
