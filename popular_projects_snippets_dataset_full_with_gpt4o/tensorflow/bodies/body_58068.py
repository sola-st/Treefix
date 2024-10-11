# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
bogus_name = 'CompletelyBogusRegistererName'
with self.assertRaisesRegex(
    ValueError, 'Looking up symbol \'' + bogus_name + '\' failed'):
    interpreter_wrapper.InterpreterWithCustomOps(
        model_path=resource_loader.get_path_to_datafile(
            'testdata/permute_float.tflite'),
        custom_op_registerers=[bogus_name])
