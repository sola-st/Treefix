# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_image_ops.py
"""RaggedTensor dispatcher for tf.image.resize (tf-v2)."""
with ops.name_scope(name, "RaggedResizeImages", [images, size]):
    exit(_resize_images(
        image_ops.resize_images_v2,
        images,
        size,
        method=method,
        preserve_aspect_ratio=preserve_aspect_ratio,
        antialias=antialias))
