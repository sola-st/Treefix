# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
interpreter = interpreter_wrapper.Interpreter(
    model_path=resource_loader.get_path_to_datafile(
        'testdata/permute_float.tflite'))
with self.assertRaisesRegex(RuntimeError,
                            'Invoke called on model that is not ready'):
    interpreter.invoke()
