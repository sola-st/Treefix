# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
input_str = 'inputx=file[[v1]v2'
with self.assertRaises(RuntimeError):
    saved_model_cli.preprocess_inputs_arg_string(input_str)
input_str = 'inputx:file'
with self.assertRaises(RuntimeError):
    saved_model_cli.preprocess_inputs_arg_string(input_str)
input_str = 'inputx:np.zeros((5))'
with self.assertRaisesRegex(RuntimeError, 'format is incorrect'):
    saved_model_cli.preprocess_input_exprs_arg_string(input_str, safe=False)
