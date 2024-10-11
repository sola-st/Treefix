# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
super().__init__()
self.size = size
# variable initialized by a Tensor-compatible value
self.w1 = variables.Variable(
    constant_op.constant(1., shape=[self.size]), trainable=False)
# variable initialized by a function
self.w2 = variables.Variable(
    lambda: constant_op.constant(2., shape=[self.size]))
# variable instantiated lazily in call()
self.w3 = None
