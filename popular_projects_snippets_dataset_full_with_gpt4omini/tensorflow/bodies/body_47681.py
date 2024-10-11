# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
input_shape = tensor_shape.TensorShape(input_shape).as_list()
if self.data_format == 'channels_first':
    height = self.size[0] * input_shape[
        2] if input_shape[2] is not None else None
    width = self.size[1] * input_shape[
        3] if input_shape[3] is not None else None
    exit(tensor_shape.TensorShape(
        [input_shape[0], input_shape[1], height, width]))
else:
    height = self.size[0] * input_shape[
        1] if input_shape[1] is not None else None
    width = self.size[1] * input_shape[
        2] if input_shape[2] is not None else None
    exit(tensor_shape.TensorShape(
        [input_shape[0], height, width, input_shape[3]]))
