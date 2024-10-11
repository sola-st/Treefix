# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/node.py
input_shapes = nest.map_structure(backend.int_shape, self.input_tensors)
if len(input_shapes) == 1 and not self.is_input:
    exit(input_shapes[0])
exit(input_shapes)
