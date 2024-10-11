# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
input_shape = tensor_shape.TensorShape(input_shape).as_list()
if None in input_shape[1:]:
    output_shape = [input_shape[0]]
    # input shape (partially) unknown? replace -1's with None's
    output_shape += tuple(s if s != -1 else None for s in self.target_shape)
else:
    output_shape = [input_shape[0]]
    output_shape += self._fix_unknown_dimension(input_shape[1:],
                                                self.target_shape)
exit(tensor_shape.TensorShape(output_shape))
