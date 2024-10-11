# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
prefix = "tensorflow/core/lib"
paths = ("png/testdata/lena_gray.png", "jpeg/testdata/jpeg_merge_test1.jpg",
         "gif/testdata/lena.gif")
decoders = {
    "jpeg": functools.partial(image_ops.decode_jpeg, channels=3),
    "png": functools.partial(image_ops.decode_png, channels=3),
    "gif": lambda s: array_ops.squeeze(image_ops.decode_gif(s), axis=0),
}
with self.cached_session():
    for path in paths:
        contents = self.evaluate(io_ops.read_file(os.path.join(prefix, path)))
        images = {}
        for name, decode in decoders.items():
            image = self.evaluate(decode(contents))
            self.assertEqual(image.ndim, 3)
            for prev_name, prev in images.items():
                print("path %s, names %s %s, shapes %s %s" %
                      (path, name, prev_name, image.shape, prev.shape))
                self.assertAllEqual(image, prev)
            images[name] = image
