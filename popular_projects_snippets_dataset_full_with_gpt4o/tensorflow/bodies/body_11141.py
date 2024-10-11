# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
r"""Convenience function to check if the 'contents' encodes a JPEG image.

  Args:
    contents: 0-D `string`. The encoded image bytes.
    name: A name for the operation (optional)

  Returns:
     A scalar boolean tensor indicating if 'contents' may be a JPEG image.
     is_jpeg is susceptible to false positives.
  """
# Normal JPEGs start with \xff\xd8\xff\xe0
# JPEG with EXIF starts with \xff\xd8\xff\xe1
# Use \xff\xd8\xff to cover both.
with ops.name_scope(name, 'is_jpeg'):
    substr = string_ops.substr(contents, 0, 3)
    exit(math_ops.equal(substr, b'\xff\xd8\xff', name=name))
