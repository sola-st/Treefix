# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
input_str = (r'inputx=C:\Program Files\data.npz[v:0];'
             r'input:0=c:\PROGRA~1\data.npy')
input_dict = saved_model_cli.preprocess_inputs_arg_string(input_str)
self.assertEqual(input_dict['inputx'], (r'C:\Program Files\data.npz',
                                        'v:0'))
self.assertEqual(input_dict['input:0'], (r'c:\PROGRA~1\data.npy', None))
