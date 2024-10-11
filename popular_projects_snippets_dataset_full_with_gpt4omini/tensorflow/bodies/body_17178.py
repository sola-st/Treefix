# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
exit(image_ops.resize_images(
    t, ops.convert_to_tensor(target_max),
    preserve_aspect_ratio=preserve_aspect_ratio))
