# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/draw_bounding_box_op_test.py
"""Tests if cycling works appropriately.

    Args:
      img: 3-D numpy image on which to draw.
      dtype: image dtype (float, half).
      colors: color table.
    """
color_table = colors
if colors is None:
    # THIS TABLE MUST MATCH draw_bounding_box_op.cc
    color_table = np.asarray([[1, 1, 0, 1], [0, 0, 1, 1], [1, 0, 0, 1],
                              [0, 1, 0, 1], [0.5, 0, 0.5,
                                             1], [0.5, 0.5, 0, 1],
                              [0.5, 0, 0, 1], [0, 0, 0.5, 1], [0, 1, 1, 1],
                              [1, 0, 1, 1]])
assert len(img.shape) == 3
depth = img.shape[2]
assert depth <= color_table.shape[1]
assert depth == 1 or depth == 3 or depth == 4
## Set red channel to 1 if image is GRY.
if depth == 1:
    color_table[:, 0] = 1
num_colors = color_table.shape[0]
for num_boxes in range(1, num_colors + 2):
    # Generate draw_bounding_box_op drawn image
    image = np.copy(img)
    color = color_table[(num_boxes - 1) % num_colors, 0:depth]
    test_drawn_image = self._fillBorder(image, color)
    bboxes = np.asarray([0, 0, 1, 1])
    bboxes = np.vstack([bboxes for _ in range(num_boxes)])
    bboxes = math_ops.cast(bboxes, dtypes.float32)
    bboxes = array_ops.expand_dims(bboxes, 0)
    image = ops.convert_to_tensor(image)
    image = image_ops_impl.convert_image_dtype(image, dtype)
    image = array_ops.expand_dims(image, 0)
    image = image_ops.draw_bounding_boxes(image, bboxes, colors=colors)
    with self.cached_session(use_gpu=False) as sess:
        op_drawn_image = np.squeeze(sess.run(image), 0)
        self.assertAllEqual(test_drawn_image, op_drawn_image)
