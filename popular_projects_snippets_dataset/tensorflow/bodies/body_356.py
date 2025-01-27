# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
# pylint: disable=line-too-long
text = "tf.image.sample_distorted_bounding_box(a, b, c, d, e, f, g, h, i, j)"
expected = "tf.image.sample_distorted_bounding_box(image_size=a, bounding_boxes=b, seed=c, min_object_covered=e, aspect_ratio_range=f, area_range=g, max_attempts=h, use_image_if_no_bounding_boxes=i, name=j)"
# pylint: enable=line-too-long
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected, new_text)
