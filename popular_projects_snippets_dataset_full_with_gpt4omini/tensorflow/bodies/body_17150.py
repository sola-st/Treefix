# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
original_area = float(np.prod(image.shape))
bounding_box_area = float((bounding_box[3] - bounding_box[1]) *
                          (bounding_box[2] - bounding_box[0]))

image_size_np = np.array(image.shape, dtype=np.int32)
bounding_box_np = (
    np.array(bounding_box, dtype=np.float32).reshape([1, 1, 4]))

aspect_ratios = []
area_ratios = []

fraction_object_covered = []

num_iter = 1000
with self.cached_session():
    image_tf = constant_op.constant(image, shape=image.shape)
    image_size_tf = constant_op.constant(
        image_size_np, shape=image_size_np.shape)
    bounding_box_tf = constant_op.constant(
        bounding_box_np, dtype=dtypes.float32, shape=bounding_box_np.shape)

    begin, size, _ = image_ops.sample_distorted_bounding_box(
        image_size=image_size_tf,
        bounding_boxes=bounding_box_tf,
        min_object_covered=min_object_covered,
        aspect_ratio_range=aspect_ratio_range,
        area_range=area_range)
    y = array_ops.strided_slice(image_tf, begin, begin + size)

    for _ in range(num_iter):
        y_tf = self.evaluate(y)
        crop_height = y_tf.shape[0]
        crop_width = y_tf.shape[1]
        aspect_ratio = float(crop_width) / float(crop_height)
        area = float(crop_width * crop_height)

        aspect_ratios.append(aspect_ratio)
        area_ratios.append(area / original_area)
        fraction_object_covered.append(float(np.sum(y_tf)) / bounding_box_area)

    # min_object_covered as tensor
    min_object_covered_t = ops.convert_to_tensor(min_object_covered)
    begin, size, _ = image_ops.sample_distorted_bounding_box(
        image_size=image_size_tf,
        bounding_boxes=bounding_box_tf,
        min_object_covered=min_object_covered_t,
        aspect_ratio_range=aspect_ratio_range,
        area_range=area_range)
    y = array_ops.strided_slice(image_tf, begin, begin + size)

    for _ in range(num_iter):
        y_tf = self.evaluate(y)
        crop_height = y_tf.shape[0]
        crop_width = y_tf.shape[1]
        aspect_ratio = float(crop_width) / float(crop_height)
        area = float(crop_width * crop_height)

        aspect_ratios.append(aspect_ratio)
        area_ratios.append(area / original_area)
        fraction_object_covered.append(float(np.sum(y_tf)) / bounding_box_area)

    # Ensure that each entry is observed within 3 standard deviations.
    # num_bins = 10
    # aspect_ratio_hist, _ = np.histogram(aspect_ratios,
    #                                     bins=num_bins,
    #                                     range=aspect_ratio_range)
    # mean = np.mean(aspect_ratio_hist)
    # stddev = np.sqrt(mean)
    # TODO(wicke, shlens, dga): Restore this test so that it is no longer flaky.
    # TODO(irving): Since the rejection probability is not independent of the
    # aspect ratio, the aspect_ratio random value is not exactly uniformly
    # distributed in [min_aspect_ratio, max_aspect_ratio).  This test should be
    # fixed to reflect the true statistical property, then tightened to enforce
    # a stricter bound.  Or, ideally, the sample_distorted_bounding_box Op
    # be fixed to not use rejection sampling and generate correctly uniform
    # aspect ratios.
    # self.assertAllClose(aspect_ratio_hist,
    #                     [mean] * num_bins, atol=3.6 * stddev)

    # The resulting crop will not be uniformly distributed in area. In practice,
    # we find that the area skews towards the small sizes. Instead, we perform
    # a weaker test to ensure that the area ratios are merely within the
    # specified bounds.
self.assertLessEqual(max(area_ratios), area_range[1])
self.assertGreaterEqual(min(area_ratios), area_range[0])

# For reference, here is what the distribution of area ratios look like.
area_ratio_hist, _ = np.histogram(area_ratios, bins=10, range=area_range)
print("area_ratio_hist ", area_ratio_hist)
