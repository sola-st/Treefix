# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
super().__init__()
self.a_variable = trackable_utils.add_variable(
    self, name="a_variable", shape=[])
