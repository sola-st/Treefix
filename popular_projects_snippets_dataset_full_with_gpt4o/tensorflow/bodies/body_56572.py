# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/convert_image_to_csv.py
for image_file_name in FLAGS.image_file_names:
    try:
        image_data = get_image(FLAGS.width, FLAGS.height, FLAGS.want_grayscale,
                               image_file_name)
        print(array_to_int_csv(image_data))
    except NotFoundError:
        sys.stderr.write("Image file not found at {0}\n".format(image_file_name))
        sys.exit(1)
