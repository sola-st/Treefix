# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test_util.py
super(SimpleModelWithOneVariable, self).__init__()
self.var = variables.Variable(array_ops.zeros((1, 10), name='var'))
