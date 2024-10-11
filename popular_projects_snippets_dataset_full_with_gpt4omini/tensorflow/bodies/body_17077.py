# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Shape function requires placeholders and a graph.
with ops.Graph().as_default():
    p_unknown_rank = array_ops.placeholder(dtypes.uint8)
    p_unknown_dims_3 = array_ops.placeholder(
        dtypes.uint8, shape=[None, None, None])
    p_unknown_dims_4 = array_ops.placeholder(
        dtypes.uint8, shape=[None, None, None, None])
    p_unknown_width = array_ops.placeholder(dtypes.uint8, shape=[64, None, 3])
    p_unknown_batch = array_ops.placeholder(
        dtypes.uint8, shape=[None, 64, 64, 3])
    p_wrong_rank = array_ops.placeholder(dtypes.uint8, shape=[None, None])
    p_zero_dim = array_ops.placeholder(dtypes.uint8, shape=[64, 0, 3])

    #Ops that support 3D input
    for op in [
        image_ops.flip_left_right, image_ops.flip_up_down,
        image_ops.random_flip_left_right, image_ops.random_flip_up_down,
        image_ops.transpose, image_ops.rot90
    ]:
        transformed_unknown_rank = op(p_unknown_rank)
        self.assertIsNone(transformed_unknown_rank.get_shape().ndims)
        transformed_unknown_dims_3 = op(p_unknown_dims_3)
        self.assertEqual(3, transformed_unknown_dims_3.get_shape().ndims)
        transformed_unknown_width = op(p_unknown_width)
        self.assertEqual(3, transformed_unknown_width.get_shape().ndims)

        with self.assertRaisesRegex(ValueError, "must be > 0"):
            op(p_zero_dim)

      #Ops that support 4D input
    for op in [
        image_ops.flip_left_right, image_ops.flip_up_down,
        image_ops.random_flip_left_right, image_ops.random_flip_up_down,
        image_ops.transpose, image_ops.rot90
    ]:
        transformed_unknown_dims_4 = op(p_unknown_dims_4)
        self.assertEqual(4, transformed_unknown_dims_4.get_shape().ndims)
        transformed_unknown_batch = op(p_unknown_batch)
        self.assertEqual(4, transformed_unknown_batch.get_shape().ndims)
        with self.assertRaisesRegex(ValueError,
                                    "must be at least three-dimensional"):
            op(p_wrong_rank)
