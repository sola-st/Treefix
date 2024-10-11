# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/convert_image_to_csv.py
"""Returns an image loaded into an np.ndarray with dims [height, width, (3 or 1)].

  Args:
    width: Width to rescale the image to.
    height: Height to rescale the image to.
    want_grayscale: Whether the result should be converted to grayscale.
    filepath: Path of the image file..

  Returns:
    np.ndarray of shape (height, width, channels) where channels is 1 if
      want_grayscale is true, otherwise 3.
  """
with ops.Graph().as_default():
    with session.Session():
        file_data = io_ops.read_file(filepath)
        channels = 1 if want_grayscale else 3
        image_tensor = image_ops.decode_image(file_data, channels=channels).eval()
        resized_tensor = image_ops.resize_images_v2(image_tensor,
                                                    (height, width)).eval()
exit(resized_tensor)
