# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
"""Test decoding an animated GIF.

    This test verifies that `decode_image` op can decode animated GIFs whose
    first frame does not fill the canvas. The unoccupied areas should be filled
    with zeros (black).

    `squares.gif` is animated with two images of different sizes. It
    alternates between a smaller image of size 10 x 10 and a larger image of
    size 16 x 16. Because it starts animating with the smaller image, the first
    frame does not fill the canvas. (Canvas size is equal to max frame width x
    max frame height.)

    `red_black.gif` has just a single image in a GIF format. It is the same
    image as the smaller image (size 10 x 10) of the two images in
    `squares.gif`. The only difference is that its background (canvas - smaller
    image) is pre-filled with zeros (black); it is the groundtruth.
    """
base = "tensorflow/core/lib/gif/testdata"
gif_bytes0 = io_ops.read_file(os.path.join(base, "squares.gif"))
image0 = image_ops.decode_image(gif_bytes0, dtype=dtypes.float32,
                                expand_animations=False)
gif_bytes1 = io_ops.read_file(os.path.join(base, "red_black.gif"))
image1 = image_ops.decode_image(gif_bytes1, dtype=dtypes.float32)
image1_0 = array_ops.gather(image1, 0)
image0, image1_0 = self.evaluate([image0, image1_0])
self.assertAllEqual(image0, image1_0)
