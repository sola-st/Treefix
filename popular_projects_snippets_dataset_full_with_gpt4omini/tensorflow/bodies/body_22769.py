# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding_test.py
bad_proto_data = b'\x0f'
with self.assertRaises(DecodeError):
    xla_sharding.get_sharding_tile_shape(bad_proto_data)
