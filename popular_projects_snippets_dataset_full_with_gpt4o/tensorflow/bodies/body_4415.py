# Extracted from ./data/repos/tensorflow/tensorflow/examples/adding_an_op/cuda_op_test.py
if tf.test.is_built_with_cuda():
    result = cuda_op.add_one([5, 4, 3, 2, 1])
    self.assertAllEqual(result, [6, 5, 4, 3, 2])
