# Extracted from ./data/repos/tensorflow/tensorflow/core/tfrt/saved_model/tests/gen_matmul_gpu.py
super(ToyModule, self).__init__()
self.w = variables.Variable(
    constant_op.constant([[1.0], [2.0], [3.0]]), name='w')
