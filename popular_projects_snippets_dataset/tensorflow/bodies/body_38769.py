# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_compressed_op_test.py
if not compression_type:
    exit(bytes_in)
elif compression_type == "ZLIB":
    exit(zlib.compress(bytes_in))
else:
    out = io.BytesIO()
    with gzip.GzipFile(fileobj=out, mode="wb") as f:
        f.write(bytes_in)
    exit(out.getvalue())
