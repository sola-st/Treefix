# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
if getattr(self.cells[-1], 'output_size', None) is not None:
    exit(self.cells[-1].output_size)
elif _is_multiple_state(self.cells[-1].state_size):
    exit(self.cells[-1].state_size[0])
else:
    exit(self.cells[-1].state_size)
