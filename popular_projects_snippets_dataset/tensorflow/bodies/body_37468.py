# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_v1_image_op_test.py
"""Verify that the non-image parts of the image_summ proto match shape."""
# Only the first 3 images are returned.
for v in image_summ.value:
    v.image.ClearField("encoded_image_string")
expected = "\n".join("""
        value {
          tag: "img/image/%d"
          image { height: %d width: %d colorspace: %d }
        }""" % ((i,) + shape[1:]) for i in range(3))
self.assertProtoEquals(expected, image_summ)
