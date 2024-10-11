# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
model, calibration_gen = self._createReadAssignModel(number_of_states)

converter = lite.TFLiteConverterV2.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = calibration_gen
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type = tf.int8  # or tf.uint8
converter.inference_output_type = tf.int8  # or tf.uint8
converter._experimental_variable_quantization = variable_quantization

converter.convert()
