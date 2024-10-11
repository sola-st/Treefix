# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert.py
"""Main in tflite_convert.py."""
use_v2_converter = tf2.enabled()
parser = _get_parser(use_v2_converter)
tflite_flags, unparsed = parser.parse_known_args(args=sys.argv[1:])

# If the user is running TensorFlow 2.X but has passed in enable_v1_converter
# then parse the flags again with the 1.X converter flags.
if tf2.enabled() and tflite_flags.enable_v1_converter:
    use_v2_converter = False
    parser = _get_parser(use_v2_converter)
    tflite_flags, unparsed = parser.parse_known_args(args=sys.argv[1:])

# Checks if the flags are valid.
try:
    if use_v2_converter:
        _check_tf2_flags(tflite_flags)
    else:
        _check_tf1_flags(tflite_flags, unparsed)
except ValueError as e:
    parser.print_usage()
    file_name = os.path.basename(sys.argv[0])
    sys.stderr.write("{0}: error: {1}\n".format(file_name, str(e)))
    sys.exit(1)

# Convert the model according to the user provided flag.
if use_v2_converter:
    _convert_tf2_model(tflite_flags)
else:
    try:
        _convert_tf1_model(tflite_flags)
    finally:
        if tflite_flags.conversion_summary_dir:
            if tflite_flags.experimental_new_converter:
                gen_html.gen_conversion_log_html(tflite_flags.conversion_summary_dir,
                                                 tflite_flags.post_training_quantize,
                                                 tflite_flags.output_file)
            else:
                warnings.warn(
                    "Conversion summary will only be generated when enabling"
                    " the new converter via --experimental_new_converter. ")
