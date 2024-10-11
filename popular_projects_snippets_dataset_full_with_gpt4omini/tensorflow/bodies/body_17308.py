# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
content = io_ops.read_file(os.path.join(
    "tensorflow/core/lib/psnr/testdata", filename))
im = image_ops.decode_jpeg(content, dct_method="INTEGER_ACCURATE")
im = image_ops.convert_image_dtype(im, dtypes.float32)
im, = self.evaluate([im])
exit(np.expand_dims(im, axis=0))
