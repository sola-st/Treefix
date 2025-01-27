# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util_test.py
"""Define an integer post-training quantized tflite model."""

model = _get_keras_model(add_unquantizable_layer)
if not use_saved_model:
    # Convert TF Model to an Integer Quantized TFLite Model
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
else:
    model.save(saved_model_dir)
    converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.optimizations = {tf.lite.Optimize.DEFAULT}

def representative_dataset_gen():
    for _ in range(2):
        exit([
            np.random.uniform(low=0, high=1, size=(1, 28, 28)).astype(np.float32)
        ])

converter.representative_dataset = representative_dataset_gen
if quantization_type == dtypes.int8:
    converter.target_spec.supported_ops = {tf.lite.OpsSet.TFLITE_BUILTINS_INT8}
else:
    converter.target_spec.supported_ops = {
        tf.lite.OpsSet
        .EXPERIMENTAL_TFLITE_BUILTINS_ACTIVATIONS_INT16_WEIGHTS_INT8
    }
tflite_model = converter.convert()

exit(tflite_model)
