# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/reverse_sequence_op_test.py
# Enter graph mode since we want to test partial shapes
with context.graph_mode():
    t = array_ops.reverse_sequence(
        array_ops.placeholder(dtypes.float32, shape=None),
        seq_lengths=array_ops.placeholder(dtypes.int64, shape=(32,)),
        batch_axis=0,
        seq_axis=1)
    self.assertIs(t.get_shape().ndims, None)
