# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Adds new Tensors to self.outputs.

    Note: this is generally unsafe to use. This is used in certain situations in
    conjunction with _set_type_list_attr.

    Args:
      types: list of DTypes
      shapes: list of TensorShapes
    """
assert len(types) == len(shapes)
orig_num_outputs = len(self.outputs)
for i in range(len(types)):
    t = Tensor(self, orig_num_outputs + i, types[i])
    self._outputs.append(t)
    t.set_shape(shapes[i])
