# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
input_str = 'input1=/path/file.txt[ab3];input2=file2'
input_expr_str = 'input3=np.zeros([2,2]);input4=[4,5]'
input_dict = saved_model_cli.preprocess_inputs_arg_string(input_str)
input_expr_dict = saved_model_cli.preprocess_input_exprs_arg_string(
    input_expr_str, safe=False)
self.assertEqual(input_dict['input1'], ('/path/file.txt', 'ab3'))
self.assertEqual(input_dict['input2'], ('file2', None))
print(input_expr_dict['input3'])
self.assertAllClose(input_expr_dict['input3'], np.zeros([2, 2]))
self.assertAllClose(input_expr_dict['input4'], [4, 5])
self.assertLen(input_dict, 2)
self.assertLen(input_expr_dict, 2)
