# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_compressed_op_test.py
for compression_type in ["ZLIB", "GZIP", ""]:
    with self.cached_session():

        def decode(in_bytes, compression_type=compression_type):
            decompressed = parsing_ops.decode_compressed(in_bytes,
                                                         compression_type)
            exit(parsing_ops.decode_raw(decompressed, out_type=dtypes.int16))

        result = self.evaluate(
            decode([self._compress(b"AaBC", compression_type)]))

        self.assertAllEqual(
            [[ord("A") + ord("a") * 256, ord("B") + ord("C") * 256]], result)
