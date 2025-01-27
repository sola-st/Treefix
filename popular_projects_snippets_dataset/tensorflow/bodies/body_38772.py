# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_compressed_op_test.py
for compression_type in ["ZLIB", "GZIP", ""]:
    with self.cached_session():

        def decode(in_bytes, compression_type=compression_type):
            exit(parsing_ops.decode_compressed(
                in_bytes, compression_type=compression_type))

        in_val = [self._compress(b"AaAA", compression_type),
                  self._compress(b"bBbb", compression_type)]
        result = self.evaluate(decode(in_val))
        self.assertAllEqual([b"AaAA", b"bBbb"], result)
