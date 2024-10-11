# Extracted from ./data/repos/tensorflow/tensorflow/core/tfrt/saved_model/tests/gen_saved_model_v2.py
super(ToyModule, self).__init__()
self.w = variables.Variable(constant_op.constant([[1], [2], [3]]), name='w')
