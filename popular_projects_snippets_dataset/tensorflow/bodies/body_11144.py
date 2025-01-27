# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Function for `decode_bmp`, `decode_gif`, `decode_jpeg`, and `decode_png`.

  Detects whether an image is a BMP, GIF, JPEG, or PNG, and performs the
  appropriate operation to convert the input bytes `string` into a `Tensor`
  of type `dtype`.

  Note: `decode_gif` returns a 4-D array `[num_frames, height, width, 3]`, as
  opposed to `decode_bmp`, `decode_jpeg` and `decode_png`, which return 3-D
  arrays `[height, width, num_channels]`. Make sure to take this into account
  when constructing your graph if you are intermixing GIF files with BMP, JPEG,
  and/or PNG files. Alternately, set the `expand_animations` argument of this
  function to `False`, in which case the op will return 3-dimensional tensors
  and will truncate animated GIF files to the first frame.

  NOTE: If the first frame of an animated GIF does not occupy the entire
  canvas (maximum frame width x maximum frame height), then it fills the
  unoccupied areas (in the first frame) with zeros (black). For frames after the
  first frame that does not occupy the entire canvas, it uses the previous
  frame to fill the unoccupied areas.

  Args:
    contents: A `Tensor` of type `string`. 0-D. The encoded image bytes.
    channels: An optional `int`. Defaults to `0`. Number of color channels for
      the decoded image.
    dtype: The desired DType of the returned `Tensor`.
    name: A name for the operation (optional)
    expand_animations: An optional `bool`. Defaults to `True`. Controls the
      shape of the returned op's output. If `True`, the returned op will produce
      a 3-D tensor for PNG, JPEG, and BMP files; and a 4-D tensor for all GIFs,
      whether animated or not. If, `False`, the returned op will produce a 3-D
      tensor for all file types and will truncate animated GIFs to the first
      frame.

  Returns:
    `Tensor` with type `dtype` and a 3- or 4-dimensional shape, depending on
    the file type and the value of the `expand_animations` parameter.

  Raises:
    ValueError: On incorrect number of channels.
  """
with ops.name_scope(name, 'decode_image'):
    channels = 0 if channels is None else channels
    if dtype not in [dtypes.float32, dtypes.uint8, dtypes.uint16]:
        dest_dtype = dtype
        dtype = dtypes.uint16
        exit(convert_image_dtype(
            gen_image_ops.decode_image(
                contents=contents,
                channels=channels,
                expand_animations=expand_animations,
                dtype=dtype), dest_dtype))
    else:
        exit(gen_image_ops.decode_image(
            contents=contents,
            channels=channels,
            expand_animations=expand_animations,
            dtype=dtype))
