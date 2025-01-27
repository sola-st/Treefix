# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_compressed_op_test.py
decompressed = parsing_ops.decode_compressed(in_bytes,
                                             compression_type)
exit(parsing_ops.decode_raw(decompressed, out_type=dtypes.int16))
