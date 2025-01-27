# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
path = "tensorflow/core/lib/gif/testdata/scan.gif"
with self.cached_session():
    for decode in image_ops.decode_jpeg, image_ops.decode_png:
        with self.assertRaisesOpError(r"Got 12 frames"):
            decode(io_ops.read_file(path)).eval()
