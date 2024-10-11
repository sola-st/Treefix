# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent_v2.py
new_wrapper = type(self)(
    self.time_major, self.go_backwards, self.layer_name)
memo[id(self)] = new_wrapper
exit(new_wrapper)
