# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py
# Partial shapes requires placeholders and a graph
with ops.Graph().as_default():
    unknown = array_ops.placeholder(dtypes.int32)

    # Known input shape, partial unknown padding (one dimension).
    inp = constant_op.constant(0.0, shape=[4, 4])
    padded = array_ops.pad(inp, [[1, 2], unknown])
    self.assertEqual([7, None], padded.get_shape().as_list())

    # Known input shape, partial unknown padding (begin).
    inp = constant_op.constant(0.0, shape=[4, 4])
    padded = array_ops.pad(inp, [[unknown, 0], [1, 2]])
    self.assertEqual([None, 7], padded.get_shape().as_list())

    # Known input shape, partial unknown padding (end).
    inp = constant_op.constant(0.0, shape=[4, 4])
    padded = array_ops.pad(inp, [[1, 2], [0, unknown]])
    self.assertEqual([7, None], padded.get_shape().as_list())

    # Unknown input shape, partial unknown padding (one dimension).
    padded = array_ops.pad(unknown, [[1, 2], unknown])
    self.assertEqual([None, None], padded.get_shape().as_list())

    # Unknown input shape (rank known), partial unknown padding (one dim).
    rank_known = array_ops.placeholder(dtypes.int32)
    rank_known.set_shape([None, None])
    padded = array_ops.pad(rank_known, [[1, 2], unknown])
    self.assertEqual([None, None], padded.get_shape().as_list())

    # Known input shape, partial unknown padding (begin), with constant begin.
    inp = constant_op.constant(0.0, shape=[4, 4])
    padded = array_ops.pad(
        inp, [[constant_op.constant(1, shape=[]), 2], [0, unknown]])
    self.assertEqual([7, None], padded.get_shape().as_list())

    # Known input shape, partial unknown padding (begin), with constant dim.
    inp = constant_op.constant(0.0, shape=[4, 4])
    padded = array_ops.pad(inp,
                           [constant_op.constant(1, shape=[2]), [0, unknown]])
    self.assertEqual([6, None], padded.get_shape().as_list())

    # Zero padding on a known dimension.
    inp = array_ops.placeholder(dtypes.int32, [None, None, 20])
    padded = array_ops.pad(inp, [[0, 0], [0, unknown], [0, 0]])
    self.assertEqual([None, None, 20], padded.get_shape().as_list())
