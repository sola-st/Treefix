# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
interpreter = interpreter_wrapper.Interpreter(
    model_path=resource_loader.get_path_to_datafile('testdata/pc_conv.bin'))
interpreter.allocate_tensors()

# Tensor index 1 is the weight.
weight_details = interpreter.get_tensor_details()[1]
qparams = weight_details['quantization_parameters']
# Ensure that we retrieve per channel quantization params correctly.
self.assertEqual(len(qparams['scales']), 128)
