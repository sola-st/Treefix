# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/annotate_max_batch_sizes_test.py
"""Builds a tf.Graph for the test."""
tensor = inp * 2.0
tensor = array_ops.reshape(tensor, [-1] + self.tensor_shapes[1][1:])
with ops.get_default_graph()._attr_scope({
    '_tftrt_op_max_batch_size':
        attr_value_pb2.AttrValue(i=self.max_batch_sizes[1])
}):
    tensor = tensor + 3.0
tensor = array_ops.reshape(tensor, [-1] + self.tensor_shapes[2][1:])
with ops.get_default_graph()._attr_scope({
    '_tftrt_op_max_batch_size':
        attr_value_pb2.AttrValue(i=self.max_batch_sizes[2])
}):
    tensor = tensor * 4.0
tensor = array_ops.reshape(tensor, [-1] + self.tensor_shapes[3][1:])
with ops.get_default_graph()._attr_scope({
    '_tftrt_op_max_batch_size':
        attr_value_pb2.AttrValue(i=self.max_batch_sizes[3])
}):
    tensor += tensor + 5.0
exit(array_ops.identity(tensor, name='output_0'))
