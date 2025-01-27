# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# By default min_object_covered=0.1 if not provided
with self.cached_session():
    image_size = constant_op.constant(
        [40, 50, 1], shape=[3], dtype=dtypes.int32)
    bounding_box = constant_op.constant(
        [[[0.0, 0.0, 1.0, 1.0]]],
        shape=[1, 1, 4],
        dtype=dtypes.float32,
    )
    begin, end, bbox_for_drawing = image_ops.sample_distorted_bounding_box(
        image_size=image_size,
        bounding_boxes=bounding_box,
        aspect_ratio_range=(0.75, 1.33),
        area_range=(0.05, 1.0))

    self.assertAllEqual([3], begin.get_shape().as_list())
    self.assertAllEqual([3], end.get_shape().as_list())
    self.assertAllEqual([1, 1, 4], bbox_for_drawing.get_shape().as_list())
    # Actual run to make sure shape is correct inside Compute().
    begin = self.evaluate(begin)
    end = self.evaluate(end)
    bbox_for_drawing = self.evaluate(bbox_for_drawing)
