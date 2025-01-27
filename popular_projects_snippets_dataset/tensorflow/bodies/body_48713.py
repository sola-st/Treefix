# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/node.py
exit(nest.map_structure(backend.int_shape, self.output_tensors))
