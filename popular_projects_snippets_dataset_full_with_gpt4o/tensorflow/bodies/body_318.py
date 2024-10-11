# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = (
    "tf.extract_image_patches(images, ksizes=ksizes, strides=strides,"
    "rates=rates, padding=padding, name=name)")
expected_text = (
    "tf.image.extract_patches(images, sizes=ksizes, strides=strides,"
    "rates=rates, padding=padding, name=name)")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
