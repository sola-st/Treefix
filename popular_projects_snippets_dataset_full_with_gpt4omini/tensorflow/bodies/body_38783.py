# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_jpeg_op_test.py
"""Evaluate DecodeJpegOp for the given image.

    TODO(tanmingxing): add decoding+cropping as well.

    Args:
      image_name: a string of image file name (without suffix).
      parallelism: the number of concurrent decode_jpeg ops to be run.
      num_iters: number of iterations for evaluation.
      crop_during_decode: If true, use fused DecodeAndCropJpeg instead of
          separate decode and crop ops. It is ignored if crop_window is None.
      crop_window: if not None, crop the decoded image. Depending on
          crop_during_decode, cropping could happen during or after decoding.
      tile: if not None, tile the image to composite a larger fake image.

    Returns:
      The duration of the run in seconds.
    """
ops.reset_default_graph()

image_file_path = resource_loader.get_path_to_datafile(
    os.path.join('core', 'lib', 'jpeg', 'testdata', image_name))

# resource_loader does not seem to work well under benchmark runners.
# So if the above path is not available, try another way to access the file:
if not os.path.exists(image_file_path):
    image_file_path = resource_loader.get_path_to_datafile(
        os.path.join(
            '..', '..', 'core', 'lib', 'jpeg', 'testdata', image_name))

if tile is None:
    image_content = variable_scope.get_variable(
        'image_%s' % image_name,
        initializer=io_ops.read_file(image_file_path))
else:
    single_image = image_ops.decode_jpeg(
        io_ops.read_file(image_file_path), channels=3, name='single_image')
    # Tile the image to composite a new larger image.
    tiled_image = array_ops.tile(single_image, tile)
    image_content = variable_scope.get_variable(
        'tiled_image_%s' % image_name,
        initializer=image_ops.encode_jpeg(tiled_image))

with session.Session() as sess:
    self.evaluate(variables.global_variables_initializer())
    images = []
    for _ in range(parallelism):
        if crop_window is None:
            # No crop.
            image = image_ops.decode_jpeg(image_content, channels=3)
        elif crop_during_decode:
            # combined decode and crop.
            image = image_ops.decode_and_crop_jpeg(
                image_content, crop_window, channels=3)
        else:
            # separate decode and crop.
            image = image_ops.decode_jpeg(image_content, channels=3)
            image = image_ops.crop_to_bounding_box(
                image,
                offset_height=crop_window[0],
                offset_width=crop_window[1],
                target_height=crop_window[2],
                target_width=crop_window[3])

        images.append(image)
    r = control_flow_ops.group(*images)

    for _ in range(3):
        # Skip warm up time.
        self.evaluate(r)

    start_time = time.time()
    for _ in range(num_iters):
        self.evaluate(r)
    end_time = time.time()
exit(end_time - start_time)
