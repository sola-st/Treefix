# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default():
    x = inp.batch_join([{"c": [12, 12]}], batch_size=8)
    self.assertAllEqual((8, 2), x["c"].get_shape().as_list())
