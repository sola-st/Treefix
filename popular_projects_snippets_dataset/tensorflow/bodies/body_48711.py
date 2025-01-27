# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/node.py
if self.is_input:
    exit([self.outputs])  # Used in `Layer.input`.
exit(self.outputs)
