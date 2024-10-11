# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
interpreter = interpreter_wrapper.Interpreter(
    model_path=resource_loader.get_path_to_datafile('testdata/pc_conv.bin'))
interpreter.allocate_tensors()
weight_details = interpreter.get_tensor_details()[1]
s_params = weight_details['sparsity_parameters']
self.assertEqual(s_params, {})
