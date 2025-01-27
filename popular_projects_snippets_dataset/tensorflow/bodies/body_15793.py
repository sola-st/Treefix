# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
origin_lengths = [3, (1, 2, 1), 2, 2]
dest_lengths = [1, 1, 3, (1, 2, 1), 2, 2]
origin_values = constant_op.constant([
    b'a', b'b', b'c', b'd', b'e', b'f', b'g', b'h', b'i', b'j', b'k', b'l',
    b'm', b'n', b'o', b'p'
])
origin_shape = DynamicRaggedShape.from_lengths(
    origin_lengths)._with_num_row_partitions(3)
dest_shape = DynamicRaggedShape.from_lengths(
    dest_lengths)._with_num_row_partitions(5)

broadcaster = dynamic_ragged_shape._get_broadcaster(origin_shape,
                                                    dest_shape)

actual = broadcaster.broadcast_flat_values(origin_values)

self.assertAllEqual(origin_values, actual)
