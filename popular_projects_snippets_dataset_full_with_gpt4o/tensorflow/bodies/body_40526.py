# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
self.assertAllEqual(
    self.evaluate(ops.convert_to_tensor(left)),
    self.evaluate(ops.convert_to_tensor(right)))
