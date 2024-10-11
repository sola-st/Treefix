# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
with test_util.use_gpu():
    original_area = float(np.prod(image.shape))
    bounding_box_area = float((bounding_box[3] - bounding_box[1]) *
                              (bounding_box[2] - bounding_box[0]))

    image_size_np = np.array(image.shape, dtype=np.int32)
    bounding_box_np = (
        np.array(bounding_box, dtype=np.float32).reshape([1, 1, 4]))

    iterations = 2
    test_seeds = [(1, 2), (3, 4), (5, 6)]

    for seed in test_seeds:
        aspect_ratios = []
        area_ratios = []
        fraction_object_covered = []
        for _ in range(iterations):
            image_tf = constant_op.constant(image, shape=image.shape)
            image_size_tf = constant_op.constant(
                image_size_np, shape=image_size_np.shape)
            bounding_box_tf = constant_op.constant(bounding_box_np,
                                                   dtype=dtypes.float32,
                                                   shape=bounding_box_np.shape)
            begin, size, _ = image_ops.stateless_sample_distorted_bounding_box(
                image_size=image_size_tf,
                bounding_boxes=bounding_box_tf,
                seed=seed,
                min_object_covered=min_object_covered,
                aspect_ratio_range=aspect_ratio_range,
                area_range=area_range)
            y = array_ops.strided_slice(image_tf, begin, begin + size)
            y_tf = self.evaluate(y)
            crop_height = y_tf.shape[0]
            crop_width = y_tf.shape[1]
            aspect_ratio = float(crop_width) / float(crop_height)
            area = float(crop_width * crop_height)
            aspect_ratios.append(aspect_ratio)
            area_ratio = area / original_area
            area_ratios.append(area_ratio)
            fraction_object_covered.append(
                float(np.sum(y_tf)) / bounding_box_area)

        # Check that `area_ratio` is within valid range.
        self.assertLessEqual(area_ratio, area_range[1])
        self.assertGreaterEqual(area_ratio, area_range[0])

        # Each array should consist of one value just repeated `iteration` times
        # because the same seed is used.
        self.assertEqual(len(set(aspect_ratios)), 1)
        self.assertEqual(len(set(area_ratios)), 1)
        self.assertEqual(len(set(fraction_object_covered)), 1)
