# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
exit(TwoCompositesSpec(
    self.x_spec._batch(batch_size), self.y_spec._batch(batch_size),
    self.color))
