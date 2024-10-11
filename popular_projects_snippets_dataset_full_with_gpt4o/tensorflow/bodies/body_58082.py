# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
interpreter_wrapper.Interpreter(
    model_path=resource_loader.get_path_to_datafile(
        'testdata/permute_float.tflite'))
increase_call.assert_called_once()
