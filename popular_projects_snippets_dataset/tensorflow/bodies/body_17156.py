# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
height = 40
width = 50
image_size = [height, width, 1]
bounding_box = [0.0, 0.0, 1.0, 1.0]
image = np.arange(
    0, np.prod(image_size), dtype=np.int32).reshape(image_size)
for min_obj_covered in [0.1, constant_op.constant(0.1)]:
    self._testStatelessSampleDistortedBoundingBox(
        image,
        bounding_box,
        min_object_covered=min_obj_covered,
        aspect_ratio_range=(0.75, 1.33),
        area_range=(0.05, 1.0))
