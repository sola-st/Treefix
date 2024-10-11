# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test a model with quantized int16 reduce sum op."""
inp = tf.keras.Input([3, 3], 3, name='x')
m = tf.keras.Model(inp, tf.reduce_sum(inp, axis=-1))

converter = tf.lite.TFLiteConverter.from_keras_model(m)
converter.target_spec.supported_ops = [
    tf.lite.OpsSet
    .EXPERIMENTAL_TFLITE_BUILTINS_ACTIVATIONS_INT16_WEIGHTS_INT8
]
converter.inference_input_type = tf.int16
converter.inference_output_type = tf.int16
converter.optimizations = [tf.lite.Optimize.DEFAULT]
inputs = {
    i.name: np.random.normal(size=i.shape).astype(np.float32)
    for i in m.inputs
}
converter.representative_dataset = lambda: [inputs]
content = converter.convert()

interpreter = tf.lite.Interpreter(model_content=content)
runner = interpreter.get_signature_runner('serving_default')
y = runner(x=np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]]).astype(np.int16))
self.assertEqual([3, 6, 9], list(list(y.values())[0]))
