# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_compressed_op_test.py
with ops.Graph().as_default():
    for compression_type in ["ZLIB", "GZIP", ""]:
        with self.cached_session():
            in_bytes = array_ops.placeholder(dtypes.string, shape=[2])
            decompressed = parsing_ops.decode_compressed(
                in_bytes, compression_type=compression_type)
            self.assertEqual([2], decompressed.get_shape().as_list())
