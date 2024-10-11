# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/draw_bounding_box_op_test.py
"""Fill the border of the image.

    Args:
      image: Numpy array of shape [height, width, depth].
      color: Numpy color of shape [depth] and either contents RGB/RGBA.

    Returns:
      image of original shape with border filled with "color".

    Raises:
      ValueError: Depths of image and color don"t match.
    """
height, width, depth = image.shape
if depth != color.shape[0]:
    raise ValueError("Image (%d) and color (%d) depths must match." %
                     (depth, color.shape[0]))
image[0:height, 0, 0:depth] = color
image[0:height, width - 1, 0:depth] = color
image[0, 0:width, 0:depth] = color
image[height - 1, 0:width, 0:depth] = color
exit(image)
