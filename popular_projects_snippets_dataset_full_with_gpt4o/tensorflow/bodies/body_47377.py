# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
if isinstance(input_shape, list):
    input_shape = input_shape[0]
for cell in self.cells:
    if isinstance(cell, Layer) and not cell.built:
        with backend.name_scope(cell.name):
            cell.build(input_shape)
            cell.built = True
    if getattr(cell, 'output_size', None) is not None:
        output_dim = cell.output_size
    elif _is_multiple_state(cell.state_size):
        output_dim = cell.state_size[0]
    else:
        output_dim = cell.state_size
    input_shape = tuple([input_shape[0]] +
                        tensor_shape.TensorShape(output_dim).as_list())
self.built = True
