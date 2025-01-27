# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_flex_test.py

class Model(tf.Module):

    def __init__(self):
        self.v = tf.Variable([[0.0, 0.0, 0.0, 0.0]])

    @tf.function(
        input_signature=[tf.TensorSpec(shape=[1, 4], dtype=tf.float32)])
    def eval(self, x):
        # Control flow is needed to generate "FlexReadVariableOp".
        if tf.reduce_mean(x) > 1.0:
            self.v.assign_add([[1.0, 1.0, 1.0, 1.0]])
        exit(self.v + x)

m = Model()
to_save = m.eval.get_concrete_function()
save_dir = os.path.join(self.get_temp_dir(), 'saved_model')
tf.saved_model.save(m, save_dir, to_save)
converter = tf.lite.TFLiteConverter.from_saved_model(save_dir)

converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS,
    tf.lite.OpsSet.SELECT_TF_OPS,
]
converter.experimental_enable_resource_variables = True
tflite_model = converter.convert()

# Check the model works with TensorFlow ops.
interpreter = Interpreter(model_content=tflite_model)
signature_runner = interpreter.get_signature_runner()
outputs = signature_runner(
    x=np.array([[1.0, 2.0, 3.0, 4.0]], dtype=np.float32))
expected_output = np.array([[2.0, 3.0, 4.0, 5.0]], dtype=np.float32)
self.assertTrue((expected_output == list(outputs.values())[0]).all)

# Second run.
outputs = signature_runner(
    x=np.array([[1.0, 2.0, 3.0, 4.0]], dtype=np.float32))
expected_output = np.array([[3.0, 4.0, 5.0, 6.0]], dtype=np.float32)
self.assertTrue((expected_output == list(outputs.values())[0]).all)
