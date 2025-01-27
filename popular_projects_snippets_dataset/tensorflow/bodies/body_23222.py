# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/annotate_max_batch_sizes_test.py
"""Builds a tf.Graph for the test."""
tensor = inp * 2.0
tensor = array_ops.reshape(tensor, self.tensor_shapes[1])
tensor = tensor + 3.0
tensor = array_ops.reshape(tensor, self.tensor_shapes[2])
tensor = tensor * 4.0
tensor = array_ops.reshape(tensor, self.tensor_shapes[3])
tensor += tensor + 5.0
exit(array_ops.identity(tensor, name='output_0'))
