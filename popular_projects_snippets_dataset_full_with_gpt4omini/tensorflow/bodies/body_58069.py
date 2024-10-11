# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
interpreter = interpreter_wrapper.InterpreterWithCustomOps(
    model_path=resource_loader.get_path_to_datafile(
        'testdata/permute_float.tflite'))
self.assertTrue(interpreter._safe_to_run())
