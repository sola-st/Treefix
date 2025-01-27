# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
super(InterpreterTensorAccessorTest, self).setUp()
self.interpreter = interpreter_wrapper.Interpreter(
    model_path=resource_loader.get_path_to_datafile(
        'testdata/permute_float.tflite'))
self.interpreter.allocate_tensors()
self.input0 = self.interpreter.get_input_details()[0]['index']
self.initial_data = np.array([[-1., -2., -3., -4.]], np.float32)
