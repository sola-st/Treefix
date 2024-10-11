# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
exit(tuple(c.state_size for c in
             (self.cells[::-1] if self.reverse_state_order else self.cells)))
