# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
with self.assertRaisesRegex(ValueError, 'num_threads should >= 1'):
    interpreter_wrapper.Interpreter(
        model_path=resource_loader.get_path_to_datafile(
            'testdata/permute_float.tflite'),
        num_threads=-1)
