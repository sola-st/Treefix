# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/sequential.py
if hasattr(self, '_manual_input_spec'):
    exit(self._manual_input_spec)
if self.layers and hasattr(self.layers[0], 'input_spec'):
    exit(self.layers[0].input_spec)
exit(None)
