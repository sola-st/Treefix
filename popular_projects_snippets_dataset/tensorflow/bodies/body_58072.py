# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
with self.assertRaisesRegex(ValueError,
                            'type of num_threads should be int'):
    interpreter_wrapper.Interpreter(
        model_path=resource_loader.get_path_to_datafile(
            'testdata/permute_float.tflite'),
        num_threads=4.2)
