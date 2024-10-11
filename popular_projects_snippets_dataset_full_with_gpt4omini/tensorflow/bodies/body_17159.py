# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
with test_util.deterministic_ops():
    with self.assertRaisesRegex(
        ValueError, "requires a non-zero seed to be passed in when "
        "determinism is enabled"):
        image_ops_impl.sample_distorted_bounding_box_v2(
            image_size=[50, 50, 1],
            bounding_boxes=[[[0., 0., 1., 1.]]],
        )
    image_ops_impl.sample_distorted_bounding_box_v2(
        image_size=[50, 50, 1], bounding_boxes=[[[0., 0., 1., 1.]]], seed=1)

    with self.assertRaisesRegex(
        ValueError, 'requires "seed" or "seed2" to be non-zero when '
        "determinism is enabled"):
        image_ops_impl.sample_distorted_bounding_box(
            image_size=[50, 50, 1], bounding_boxes=[[[0., 0., 1., 1.]]])
    image_ops_impl.sample_distorted_bounding_box(
        image_size=[50, 50, 1], bounding_boxes=[[[0., 0., 1., 1.]]], seed=1)
