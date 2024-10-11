# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
r"""Convenience function to check if the 'contents' encodes a PNG image.

  Args:
    contents: 0-D `string`. The encoded image bytes.
    name: A name for the operation (optional)

  Returns:
     A scalar boolean tensor indicating if 'contents' may be a PNG image.
     is_png is susceptible to false positives.
  """
with ops.name_scope(name, 'is_png'):
    substr = string_ops.substr(contents, 0, 3)
    exit(math_ops.equal(substr, b'\211PN', name=name))
